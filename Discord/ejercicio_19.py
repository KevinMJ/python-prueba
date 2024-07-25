"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Desarrolla un algoritmo que lea un carácter cualquiera desde el teclado, y muestre el mensaje "Es una MAYÚSCULA" cuando el carácter sea una letra mayúscula y el mensaje "Es una MINÚSCULA" cuando sea una minúscula. Cuando se ingrese un carácter que no sea un carácter, muestra el mensaje "No es una letra". Recuerda que debe ser valido el carácter eñe para este ejercicio.
"""

#Inputs
word = input("Type in to discover if it is lowercase or uppercase: \n")

# Program
uppercase = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
lowercase = "abcdefghijklmnñopqrstuvxyz"

if word in uppercase:
    print(f"Your word {word} is UPPERCASE")
elif word in lowercase:
    print(f"Your word {word} is lowercase")
else:
    print("Try again maybe you are no typing a word.. :(")
