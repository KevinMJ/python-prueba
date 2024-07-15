"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Elabora un algoritmo para calcular e imprimir el precio de un terreno del cual se tienen los siguientes datos: largo, ancho, y el precio por metro cuadrado. Si el terreno tiene mas de 400 metros cuadrados, se hace un descuento de 10%.
>>>imprime el area del terreno y el precio.
"""

#Inputs
width = int(input("Type in the width of the plot of land: "))
lenght = int(input("Type in the length of the plot of land: "))
m2_price = int(input("Type in the price per square meter: "))

#Program
area = width * lenght

if area > 400: 
    price = m2_price * area * .90
else:
    price = m2_price * area

#Outputs

print(f"The plot of land has an área of {area} and is priced at ${price:.2f}")