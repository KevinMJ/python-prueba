"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ


!Dada la función (ver url)[https://i.postimg.cc/tgyBJ6xQ/imagen.png]
!Desarrolla un algoritmo que calcule la función para un valor dado de 'x' que indica dependiendo del caso.
>>> Imprime el valor de la función
"""
#Inputs
x = float(input("Type in x value: "))

#Program
if x <= 0:
    result = x**2 -x
else:
    result = -(x**2) + 3*x

#Result

print(f"f(x)= {result}")