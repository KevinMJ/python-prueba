import tkinter as tk
import os
from PIL import Image, ImageTk

# ---> Rutas
# Carpeta principal
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal,"imagenes")

class Login:
    def __init__(self):
        #Creación de la ventana
        self.root = tk.Tk()
        self.root.title("Proyecto de bases de datos")
        #self.root.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
        self.root.geometry("450x450")

        #Contenido de la ventana principal
        #Logo
        logo = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"logo.png")))
        tk.Label(self.root, image=logo).pack()

        #Campos de texto
        #Usuario
        tk.Label(self.root, text="Usuario").pack
        self.usuario = tk.Entry(self.root)
        self.usuario.insert(0, "Ej:Laura")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0,tk.END))
        self.usuario.pack()

        #Contraseña
        tk.Label(self.root, text="Contraseña").pack
        self.contrasena = tk.Entry(self.root)
        self.contrasena.insert(0, "*" * 11)
        self.contrasena.bind("<Button-1>", lambda e: self.contrasena.delete(0,tk.END))
        self.contrasena.pack()

        #Botón de envío
        self.Entrar = tk.Button(self.root, text="Entrar")
        self.Entrar.pack()
    
        #Bucle de ejecución
        self.root.mainloop()