import mysql.connector
import os
import subprocess
from datetime import datetime

# Conexion con la base de datos

acceso_bd = {"host" : "localhost",
             "user" : "root",
             "password" : "B14niet-",
             "database" : "pruebas"
             }

# --> Rutas
# Obtener la raíz de la carpeta principal
carpeta_principal = os.path.dirname(__file__)

# Directorio de los respaldos
carpeta_respaldo = os.path.join(carpeta_principal, "respaldo")

class BaseDatos:
    #Conexión y cursor
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        self.contrasena = kwargs["password"]

    #Decorador para el reporte de bases de datos del servidor
    def reporte_bd(funcion_parametro):
        def interno(self, *args):
            funcion_parametro(self, *args)
            print("Estas son las bases de datos que contiene el servidor: ")
            #Quizás te confunda la forma de llamar al método. 
            # Esto se hace así debido al alcance. 
            # Primero tengo que hacer referencia a la clase con «BaseDatos» 
            #(con self, se hace referencia al propio objeto que se instancia, no a la clase). 
            # Usando un punto, puedo indicarle qué método quiero llamar de la clase.
            BaseDatos.mostrar_bd(self)
        return interno

    #Consultas SQL
    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    # Muestra las bases de datos del servidor
    def mostrar_bd(self):
        self.cursor.execute("SHOW DATABASES")
        for bd in self.cursor:
            print(bd)
    
    #Elimina una base de datos
    @reporte_bd
    def eliminar_bd(self, base_a_eliminar):
        try:
            self.cursor.execute(f"DROP DATABASE {base_a_eliminar}")
            print(f"Se elimino la base de datos {base_a_eliminar} correctamente")
        except:
            print(f"No se ha podido eliminar {base_a_eliminar}")

    #Crea una base de datos
    @reporte_bd
    def crear_bd(self, base_a_crear):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {base_a_crear}")
            print(f"Se ha creado correctamente o ya estaba creada la base de datos: {base_a_crear}")
            print("Ahora coexisten: ")
        except:
            print(f"no se ha podido crear: {base_a_crear}.")

    #Guarda copias de seguridad
    def guardar_respaldo_bd(self,nombre_bd):
        #Obtiene la fecha y hora actual
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        with open(f'{carpeta_respaldo}/{nombre_bd}_{fecha_hora}.sql', 'w') as out: subprocess.Popen(f'"/usr/bin/"mysqldump --user=root --password={self.contrasena} --databases {nombre_bd}', shell=True, stdout=out)

    def crear_tabla(self, nombre_bd, nombre_tabla, columnas):
        #String para guardar el string con las columnas y tipos de datos
        columnas_string = ""
        # Se itera la lista que se le pasa como argumento (cada diccionario)
        for columna in columnas:
            #formamos el string con nombre, tipo y longitud
            columnas_string += f"{columna['name']} {columna['type']} ({columna['length']})"
            # Si es clave primaria, auto_increment o no admite valores nulos, lo añade al string
            if columna['primary_key']:
                columnas_string += " PRIMARY KEY"
            if columna['auto_increment']:
                columnas_string += " AUTO_INCREMENT"
            if columna['not_null']:
                columnas_string += " NOT NULL"
            #Hace un salto de lúnea después de cada diccionario
            columnas_string += ",\n"
        #Elimina al final del string el salto e línea y la coma
        columnas_string = columnas_string[:-2]
        #Le indica al que base de datos utilizar
        self.cursor.execute(f"USE {nombre_bd}")
        #Se crea la tabla juntando la instrucción SQL con el string generado
        sql = f"CREATE TABLE {nombre_tabla} ({columnas_string});"
        #Se ejecuta la instrucción
        self.cursor.execute(sql)
        #Se hace efectiva
        self.conector.commit()
        #Se cierra la conexión
        self.conector.close()

    def eliminar_tabla(self, nombre_bd, nombre_tabla):
        self.cursor.execute(f"USE {nombre_bd}")
        self.cursor.execute(f"DROP TABLE {nombre_tabla}")