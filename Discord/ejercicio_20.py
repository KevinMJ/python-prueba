"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

*tres en uno
?Crea un menú el cual contenga los 3 ejercicios. Ingresaras a cada uno de estos ingresando una entrada por la terminal, si la persona ingresa 1, ejecutara el primer ejercicio, si ingresa 2, el segundo ejercicio y si ingresa 3, el tercer ejercicio. Si la persona ingresa un valor numérico fuera de los especificados, imprime que el dato no es valido y no ejecutes ningún ejercicio.

!Escribe un programa que solicite al usuario ingresar un número y luego verifique si ese número está presente en una lista predefinida de números. Imprime un mensaje indicando si el número está o no en la lista.

!Crea un programa que pida al usuario ingresar una palabra y luego determine si esa palabra está presente en una cadena de texto predefinida. Imprime un mensaje indicando si la palabra está o no en la cadena.

!Estás desarrollando una aplicación para calcular estadísticas básicas sobre los animes que has visto. Quieres un script que tome una lista de puntuaciones de episodios y calcule el promedio y la moda.
?Restricciones
- no usar módulos, funciones, ciclos. Solo condicionales
"""

#Inputs
option = int(input("type in your choice 1, 2, 3: "))

# Program
if option == 1:
    list = 1, 2, 3
    number_to_check = int(input("Try a number between 1 - 10: "))
    if number_to_check in list:
        print(f"Congratulations {number_to_check} is on the list")
    else:
        print("Bad luck, run the program again")

if option == 2:
    word_to_check = input("Type in a word to find it in the message: ")
    message = "Hello World"
    if word_to_check in message:
        print(f"Congratulations {word_to_check} is on the message: {message}")
    else:
        print("Bad luck, run the program again")

if option == 3:
    score_1= int(input("Type in the anime episode rate: "))
    score_2= int(input("Type in the anime episode rate: "))
    score_3= int(input("Type in the anime episode rate: "))

    average = (score_1 + score_2 + score_3)/3

    print(f"the average of t rates is: {average:.2f}")
    if score_1 == score_2 or score_2 == score_3:
        print(f"The mean is {score_2}")
    elif score_3 == score_1:
        print(f"The mean is {score_1}")