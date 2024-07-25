"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Dado un numero entero, desarrolla un algoritmo para determinar si el numero es positivo, negativo o no tiene magnitud.
>>>Imprime el numero con el texto "positivo", "negativo" o "no tiene magnitud" cual sea su caso.
"""

#Inputs
number = float(input("Enter a number to determine if it is positive, negative, or has no magnitude: "))

#Program

if number > 0: 
    result = "positive"
elif number == 0:
    result = "without magnitude"
else:
    result = "negative"

#Outputs
print (f"Your number {number:.2f} is: {result}")
