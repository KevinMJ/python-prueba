"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Dado dos números enteros, desarrolla un algoritmo para determinar, si son iguales, se multiplicaran los dos números. Si el primer numero es mayor que el segundo, se restan los números; y si el primer número es menor que el segundo número, se sumaran ambos.
>>>Imprime la multiplicación, o la resta, o la suma.
"""
#Inputs
whole_number_1 = int(input("Type in a whole number: "))
whole_number_2 = int(input("Type in a whole number, again : "))

#Program
if whole_number_1 == whole_number_2:
    output = whole_number_1 * whole_number_2
elif whole_number_1 > whole_number_2:
    output = whole_number_1 - whole_number_2
else:
    output = whole_number_1 + whole_number_2

#Outputs

print(f"The result is: {output}")
