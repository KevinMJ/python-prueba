"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Desarrolla un algoritmo para el cual se da el nombre del empleado, la clave del empleado, y los 6 primeros sueldos mensuales del año. Calcula el ingreso total del semestre y el promedio mensual.
>>>Imprime la clave del empleado, nombre del empleado, ingreso total y el promedio mensual.
"""

# Inputs

employee_name = input("What is the employee name? ")
employee_id = input("What is the employee id?")
salary_1 = float(input("Enter the salary for the first paid month: "))
salary_2 = float(input("Enter the salary for the second paid month: "))
salary_3 = float(input("Enter the salary for the third paid month: "))
salary_4 = float(input("Enter the salary for the fourth paid month: "))
salary_5 = float(input("Enter the salary for the fifth paid month: "))
salary_6 = float(input("Enter the salary for the sixth paid month: "))

#Program
total_paid_salary = salary_1 + salary_2 + salary_3 + salary_4 + salary_5 + salary_6
average_month_salary = (total_paid_salary)/ 6

# Outcomes

print(f"Id: {employee_id}\nEmployee Name: {employee_name} \nTotal paid salary: ${total_paid_salary}\n Average Salary: ${average_month_salary}" )