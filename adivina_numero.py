import random
import os 
import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Creación de la ventana principal
    root = tk.Tk()

    # Personalización de la ventana principal
    root.title("Adivina el número")

    ancho_ventana = 900
    alto_ventana = 900

    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    posicion_x = int((ancho_pantalla/2)-(ancho_ventana/2))
    posicion_y = int((alto_pantalla/2)-(alto_ventana/2))

    root.geometry("{}x{}+{}+{}".format(ancho_ventana,alto_ventana,posicion_x,posicion_y))

    root.config(background="pale turquoise")

    # Frames 
    marco_bienvenida = tk.LabelFrame(root, text="Bienvenido", borderwidth= 10, background= "Khaki1",width=800,height=300)
    marco_bienvenida.pack()
    marco_Juego = tk.LabelFrame(root,borderwidth=0, background="orange",width=800,height=300)
    marco_Juego.pack()
    marco_mensajes = tk.LabelFrame(root, text="mensajes del juego", borderwidth=3, background="coral1",width=800,height=300)
    marco_mensajes.pack()

    # Carga de directorios

    directorio_principal = os.path.dirname(__file__)

    # Logo del juego
    dir_logo = os.path.join(directorio_principal, "logo.png")

    # Variables funcionales
    lista = [] # Lista para almacenar imágenes y que no se las lleve el recolector de basura
    dificultad = tk.IntVar() # Variable para seleccionar dificultad
    dificultad.set(1) # Opción por defecto
    intentos_usuario = 1


    # Mensaje de Bienvenida
    img_logo = ImageTk.PhotoImage(Image.open(dir_logo).resize((200,200)))
    etiqueta_logo = tk.Label(marco_bienvenida, image=img_logo)
    etiqueta_logo.pack()

    lista.append(img_logo)
    tk.Label(marco_bienvenida, 
             text = "Bienvenido, ¿crees poder adivinar el número en menos de 2 intentos ?", 
             font=("Helvetica", 16, "bold"),
             wraplength=(ancho_ventana-(ancho_pantalla/8)),
             background="khaki1",
             pady=10).pack(pady=10)

    # Entradas de Información
    tk.Radiobutton(marco_Juego, text= "Nivel 1", value= 1, variable=dificultad).pack()
    tk.Radiobutton(marco_Juego, text= "Nivel 2", value= 2, variable=dificultad).pack()
    tk.Radiobutton(marco_Juego, text= "Nivel 3", value= 3, variable=dificultad).pack()

    # Juego Principal
    def comenzar_juego():
        numero_computadora = 0 # inicialización

        x = dificultad.get()

        if x == 1:
            numero_computadora = numero_aleatorio(5)
        elif x == 2:
            numero_computadora = numero_aleatorio(10)
        elif x ==3:
            numero_computadora = numero_aleatorio(30)

        etiqueta_2 = tk.Label(marco_Juego,text="Adivina el Número")
        etiqueta_2.pack()
        entrada = tk.Entry(marco_Juego)
        entrada.pack()

        def adivinar(numero_usuario):
            global intentos_usuario
            if numero_usuario == numero_computadora:
                etiqueta = tk.Label(marco_mensajes,text=f"Felicidades, has acertado el número en {intentos_usuario} intentos")
                etiqueta.pack()
            else:
                intentos_usuario += 1
                if numero_usuario > numero_computadora:
                    etiqueta = tk.Label(marco_mensajes,text="menos")
                    etiqueta.pack()
                else:
                    etiqueta = tk.Label(marco_mensajes,text="menos")
                    etiqueta.pack()
                    
        bt_respuesta = tk.Button(marco_Juego, text="Adivinar", command=lambda : adivinar(int(entrada.get())))
        bt_respuesta.pack()
                
    # Botones
    bt_comenzar_juego = tk.Button(marco_Juego, command= comenzar_juego, text="Comenzar Juego")
    bt_comenzar_juego.pack()
    
    # Bucle de ejecución
    root.mainloop()

def numero_aleatorio(x):
    return random.randint(1,x)

if __name__ == "__main__":
    main()

