"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Desarrolla un algoritmo que, dados dos números enteros, muestre por pantalla uno de estos mensajes:
!- El segundo es el cuadrado exacto del primero.
!- El segundo es menor que el cuadrado del primero
!- El segundo es mayor que el cuadrado del primero.
!Dependiendo de la verificación de la condición correspondiente al significado de cada mensaje.
"""

#Inputs
number_1 = float(input("Type in number 1: "))
number_2 = float(input("Type in number 1: "))

# Program

if number_2 == (number_1**2):
    print("The second is the exact square of the first")

elif number_2 < (number_1**2):
    print("The second is less than the square of the first")

elif number_2 > (number_1**2):
    print("The second is greater than the square of the first")

else:
    print("Try again")