"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Dado un carácter alfanumérico, desarrolla un algoritmo para determinar si es una vocal o no es una vocal.
>>> Imprimir el carácter junto con el mensaje "es una vocal" o "no es una vocal".
?Restricciones
- No puedes utilizar métodos, funciones o módulos incorporados (built-in).
- Solo utilizando la estructura if-elif-else.
"""

#Inputs
word = input("Type in your word yo determine if it is vocal or not: ")

#Program
if word == "a" or word == "e" or word == "i" or word == "o" or word == "u" or word == "A" or word == "E" or word == "I" or word == "O" or word == "U":
    is_vocal = "vocal"
else:
    is_vocal = "no vocal"

#Output
print(f"your word {word} is {is_vocal}")