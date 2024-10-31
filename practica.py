from tkinter import *

# Creación de la ventana principal

root = Tk()

# Título de la ventana
root.title("Prueba de título")

nombre = Entry(root) # Para inicializar la clase Entry
nombre.insert(0, "Escriba su nombre... ") # Para poner un valor por defecto
nombre.bind("<Button-1>", lambda x : nombre.delete(0, END)) # El método bind() permite capturar un evento y asociarle una llamada a una función. Para que no se borre en automático se le agrega la función lambda -- <Key> -- <BackSpace> -- Son ejemplos de otros eventos que podríamos estar esperando.
nombre.pack()

# Tamaño de la ventana

#root.geometry("600x450+50+75")

# Evento para el botón

def pulsar_boton():
    nombre = entrada.get()
    Label(root, text="Botón Pulsado").pack()
    Label(root, text= f"{texto}").pack()

def crear_etiqueta(numero_boton):
    Label(root, text=f"Haz pulsado el botón: {numero_boton}").pack()

# Botón

Button(root, text="¡Púlsame!", command= pulsar_boton).pack() # Si aquí le agrego los paréntesis al final de la función pulsar botón, se ejecuta en automático. 

Button(root, text="Botón 1", command = lambda : crear_etiqueta(1)).pack()
Button(root, text="Botón 2", command = lambda : crear_etiqueta(2)).pack()
Button(root, text="Botón 3", command = lambda : crear_etiqueta(3)).pack()
Button(root, text="Botón 4", command = lambda : crear_etiqueta(4)).pack()

# Bucle de ejecución

root.mainloop()
