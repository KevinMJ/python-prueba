import mysql.connector
import os
import subprocess
import datetime

# Conexion con la base de datos

acceso_bd = {"host" : "localhost",
             "user" : "root",
             "password" : "B14niet-",
             }

# --> Rutas
# Obtener la raíz de la carpeta principal
carpeta_principal = os.path.dirname(__file__)

# Directorio de los respaldos
carpeta_respaldo = os.path.join(carpeta_principal, "respaldo")
print(carpeta_respaldo)

class BaseDatos:
    #Conexión y cursor
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        self.host = kwargs["host"]
        self.usuario = kwargs["user"]
        self.contrasena = kwargs["password"]
        self.conexion_cerrada = False # Variable de control para el decorador cierre

    #Decorador para el cierre del cursor y la base de datos
    def conexion(funcion_parametro):
        def interno(self, *args, **kwargs):
            try:
                # Se llama a la función externa
                if self.conexion_cerrada:
                    self.conector = mysql.connector.connect(
                        host = self.host,
                        user = self.usuario,
                        password = self.contrasena
                    )
                    self.cursor = self.conector.cursor()
                    self.conexion_cerrada = False
                    print("Se abrió la conexión con el servidor.")
                #Llamamos a la función externa
                funcion_parametro(self, *args, **kwargs)
            except:
                #Se informa de un error en la llamada
                print("Ocurrió un error en la función decoradora.")
            finally:
                if self.conexion_cerrada:
                    pass
                else:
                    #Cerramos el cursor y la conexión
                    self.cursor.close()
                    self.conector.close()
                    self.conexion_cerrada = True
                    print("Se cerró la conexión con el servidor.")
        return interno
    
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
    
    #Decorador para ver si la base de datos existe
    def existencia_bd(funcion_parametro):
        def interno(self, nombre_bd, *args):
            # Verifica si la base de datos existe
            sql = f"SHOW DATABASES LIKE '{nombre_bd}'"
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()

            #Si la base de datos no existe, muestra un mensaje de error y termina la función
            if not resultado:
                print(f"No se ha podido comprobar la existencia de la base '-> {nombre_bd} <-', por favor revisa nuevamente el nombre que has escrito")
                return
            #Ejecuta la función decorada y devuelve el resultado
            return funcion_parametro(self,nombre_bd, *args)
        return interno

    #Consultas SQL
    @conexion
    def consulta(self, sql):
        try:
            #Realiza la consulta o modificación de la base de datos
            self.cursor.execute(sql)
            print("Esta es la salida de la instrucción qe has introducido: ")
            print(self.cursor.fetchall())
        except:
            #Si ocurre una excepción se avisa en la consola
            print("Ocurrió un error. Revisa la instrucción SQL.")
    
    # Muestra las bases de datos del servidor
    @conexion
    def mostrar_bd(self):
        try:
            #Se informa de la obtención de las bases de datos y se sugiere un separador
            print("---> Listado de las bases de datos del servidor: <---")
            print("-"*80)
            #Realiza la consulta para mostrar las bases de datos
            self.cursor.execute("SHOW DATABASES")
            #Recorre los reultados y los muestra por pantalla
            for bd in self.cursor:
                print(f"-{bd[0]}.")
        except:
            print("Ocurrió un error al momento de obtener las bases de datos para mostrarlas.")

    #Elimina una base de datos
    @conexion
    @reporte_bd
    @existencia_bd
    def eliminar_bd(self, base_a_eliminar):
        try:
            #Realiza la consulta para eliminar la base de datos
            self.cursor.execute(f"DROP DATABASE {base_a_eliminar}")
            print(f"Se elimino la base de datos {base_a_eliminar} correctamente")
        except:
            #Si ocurre una excepción, se avisa en la consola
            print(f"No se ha podido eliminar {base_a_eliminar}")

    #Crea una base de datos
    @conexion
    @reporte_bd
    def crear_bd(self, base_a_crear):
        try:
            #Realiza la consulta para crear una base de datos
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {base_a_crear}")
            print(f"Se ha creado correctamente o ya estaba creada la base de datos: {base_a_crear}")
        except:
            #Si ocurre una excepción, se avisa en la consola
            print(f"no se ha podido crear: {base_a_crear}.")

    #Guarda copias de seguridad

    @conexion
    @existencia_bd
    def guardar_respaldo_bd(self, nombre_bd):        
        #Obtiene la fecha y hora actual
        self.fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        try:
            with open(f'{carpeta_respaldo}/{nombre_bd}_{self.fecha_hora}.sql', 'w') as out: subprocess.Popen(f'"/usr/bin/"mysqldump --user=root --password={self.contrasena} --databases {nombre_bd}', shell=True, stdout=out)
            print(f"Se ha generado correctamente el respaldo de la base de datos {nombre_bd}")
        except:
            print("Se ha generado un error al momento de ralizar el respaldo.")

    # Crea una tabla dentro de una base de datos especificada
    @conexion
    @existencia_bd    
    def crear_tabla(self, nombre_bd, nombre_tabla, columnas):
        try:
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
            #Informa al usuario de la creación de la tabla.
            print("Se creó la tabla correctamente.")
        except:
            print(f"No se ha podido crear la tabla: {nombre_tabla} en la siguiente base de datos: {nombre_bd}")
        
    
    #Elimina una tabla de una base de datos especificada
    @conexion
    @existencia_bd
    def eliminar_tabla(self, nombre_bd, nombre_tabla):
        self.cursor.execute(f"USE {nombre_bd}")
        try:
            self.cursor.execute(f"DROP TABLE {nombre_tabla}")
        except:
            print(f"No se ha podido eliminar la tabla de la base de datos {nombre_bd}")

    #Muestra las tablas de una base de datos
    @conexion
    @existencia_bd
    def mostrar_tablas(self, nombre_bd):
        try:
            self.cursor.execute(f"USE {nombre_bd}")
            print("Aquí tienes las tablas existentes en esa base de datos: ")
            self.cursor.execute(f"SHOW TABLES")
            resultado = self.cursor.fetchall()
            #Evalúa si hay tablas en la base de datos
            if resultado == []:
                print("No hay tablas en esta base de datos")
            else:
            # Recorre los resultados y los muestra por pantalla
                for tabla in resultado:
                    print(f"-{tabla[0]}")
        except:
            print("Revisa la instrucción para mostrar tablas")

    #Muestra las columnas de una tabla
    @conexion
    @existencia_bd
    def mostrar_columnas(self, nombre_bd, nombre_tabla):
        self.cursor.execute(f"USE {nombre_bd}")
        try:
            self.cursor.execute(f"SHOW COLUMNS FROM {nombre_tabla}")
            resultado = self.cursor.fetchall()

            print("Aquí tienes el listado de las columnas de la tabla")
            #Recorre los resultados y los muestra por pantalla
            for columna in resultado:
                #Separa los valores de la tupla para darles formato y vuelve la información explícita
                not_null = "No admite valores nulos." if columna[2] == "NO" else "Admite valores nulos."
                primary_key = "Es clave primaria" if columna[3] == "PRI" else ""
                foreign_key = "Es clave foránea." if columna[3] == "MUL" else ""

                #Imprime en pantalla la informacion de cada columna
                print(f"-{columna[0]} ({columna[1]} {not_null} {primary_key} {foreign_key})")
        except:
            print(f"Revisa haber escrito correctamente este nombre --> '{nombre_tabla}'")
    
    #Método para insertar registros en una tabla
    @conexion
    def insertar_registro(self,nombre_bd, nombre_tabla, registro):
        self.cursor.execute(f"USE {nombre_bd}")

        if not registro: # Verifica si el registro no está vacio
            print("La lista del registro está vacía")
            return
        
        # Obtener las columnas y los valores de cada diccionario
        columnas = []
        valores = []
        for registro in registro:
            columnas.extend(registro.keys())
            valores.extend(registro.values())
        
        #Convertir las columnas y los valores a strings
        columnas_string = ''
        for columna in columnas:
            columnas_string +=f"{columna}, "
        columnas_string = columnas_string[:-2] #Para quitar la última coma y el espacio

        valores_string = ''
        for valor in valores:
            valores_string += f"'{valor}', "
        valores_string = valores_string[:-2]

        #Crear la instrucción de la inserción
        sql = f"INSERT INTO {nombre_tabla} ({columnas_string}) VALUES ({valores_string})"
        self.cursor.execute(sql)
        self.conector.commit()
        print("Registro añadido en la tabla")