"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Realiza un algoritmo para calcular el sueldo de un operador de tal manera que se otorgara 
un aumento del 5% si el operador trabaja mas de 40 horas. Se tiene como datos:
? nombre del empleado
? horas de trabajo
? pago por horas trabajadas
>>>Imprimir el nombre del operador y su sueldo.
"""

# User Inputs

name = input("What is the employee name? ")
hours_worked = float(input("How many hours did the employee work? "))
salary_per_hour = float(input("How much does the employee earn per hour? "))

# Main Program

if hours_worked > 40:
    salary_to_pay = hours_worked * salary_per_hour * 1.05
    print("Good job, you earn a 5% increment to your salary!")
else:
    salary_to_pay = hours_worked * salary_per_hour

print(f"Salary to pay to {name} = {salary_to_pay:.2f}")
