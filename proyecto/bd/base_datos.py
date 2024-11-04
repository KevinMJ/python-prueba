import mysql.connector
import os
import subprocess
import getpass

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
        with open(f'{carpeta_respaldo}/{nombre_bd}.sql', 'w') as out: subprocess.Popen(f'"/usr/bin/"mysqldump --user=root --password={acceso_bd["password"]} --databases {nombre_bd}', shell=True, stdout=out)

