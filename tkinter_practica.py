from tkinter import *

root = Tk()



Label(root, text="Nombre: ").grid(row=0, column= 0)
Label(root, text="Edad: ").grid(row=1, column= 0)

nombre = Entry(root)
nombre.grid(row=0, column=1)
nombre.insert(0, "Escriba su nombre aquí.")
nombre.bind("<Button-1>", lambda x : nombre.delete(0, END))

apellido = Entry(root)
apellido.grid(row=1, column=1)
apellido.insert(0, "Escriba aquí su apellido.")
apellido.bind("<Button-1>", lambda x : nombre.delete(0, END))

Button(root, text="Saludar", command = lambda : saludo(nombre.get(), apellido.get())).grid(row=2, column=1)


def saludo(nombre, apellido):
    Label(root, text=f"¡Hola {nombre} {apellido}, bienvenido!").grid(row=3,column=1)

root.mainloop()