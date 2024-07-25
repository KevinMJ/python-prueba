"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Dado un numero entero, desarrolla un algoritmo para determinar si no es par, imprimir el mensaje 'el numero no pertenece a los pares', de lo contrario imprime 'el numero pertenece a los pares'.
"""
number = int(input("Type in an integer: ")) #Integer

if number%2 == 0: # A number that is divisible by 2 without leaving a reminder
    print(f"Your {number} is even")
else:
    print(f"Your number {number} is odd")