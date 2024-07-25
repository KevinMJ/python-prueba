"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Desarrolla un algoritmo que reciba las longitudes de los tres lados de un triángulo y determine si es equilátero, isósceles o escaleno. Además, verifica si los lados ingresados pueden formar un triángulo válido.
>>>Imprimir el tipo de triángulo o un mensaje indicando que no es un triángulo válido.
"""

# Inputs
side_A = float(input("Type the lenght of side A: "))
side_B = float(input("Type the lenght of side A: "))
side_C = float(input("Type the lenght of side A: "))

# Program
if side_A == side_B == side_C: # All sides are equal (Equilateral)
    print("It is an equilateral triangle")

elif side_A == side_B or side_B == side_C or side_A == side_C: # At least two sides are equal
    print("It is an isoceles triangle")

else:  # All sides are diferent
    print("It is an scalene triangle")