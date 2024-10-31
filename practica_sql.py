import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "B14niet-",
    database = "pruebas"
)

cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE clientes"
                    "(id INT NOT NULL AUTO_INCREMENT,"
                    "nombre VARCHAR (32) NOT NULL,"
                    "apellidos VARCHAR (64) NOT NULL,"
                    "telefono VARCHAR (9) NOT NULL,"
                    "direccion VARCHAR (256),"
                    "PRIMARY KEY (id));")   
    print("se creó correctamente la tabla.")

except:
    print("Ocurrió un error al intentar crear la tabla. Inténtelo nuevamente")