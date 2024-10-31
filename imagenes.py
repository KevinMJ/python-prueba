# Importaciones
from tkinter import *
import os  # Importar funciones para trabajar con el sistema operativo
from PIL import ImageTk, Image  # Módulo para procesar imágenes y trabajar con ellas

# ---Carga de directorios--- 
# Directorio principal
ruta_absoluta = os.path.abspath(__file__)
carpeta_principal = os.path.dirname(ruta_absoluta)  # Aquí se puede escribir la ruta directa, sin embargo utilizando __file__ quedará de forma dinámica para cuando querramos llevar el proyecto a otra computadora. En el video sugiere emplear diname, pero no me ha funcionado, solo muestra la variable correctamente, pero no la imprime en consola

# Carpeta imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title("Título de la página")

# Icono de la ventana
root.iconbitmap("/Users/kevinmelendez/Desktop/python-prueba/imagenes/favicon.ico")# Solo acepta imágenes con la extensión .ico

print(os.path.join(carpeta_imagenes, "img.ico"))

# Carga de imagen
success = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes,"success.jpg")).resize((350,200))) # Es mejor redimensionar la imagen desde su concepción y tratar de emplear lo menos posible. resize
etiqueta = Label(image=success)
etiqueta.pack()

# Bucle de ejecución
root.mainloop()

