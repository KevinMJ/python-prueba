"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!El director del departamento deportivo de una facultad esta interesado en conocer que porcentaje de mujeres y hombres hay en la facultad. Desarrolla un algoritmo para calcular los porcentajes de hombres y mujeres que hay.
>>>imprime el porcentaje de cada sexo
"""

#Inputs
men = int(input("Type in the number of men in the sports department: "))
women = int(input("Type in the number of women in the sports department: "))

#Program

total_students = men + women

percentage_male = (men / total_students) * 100 #Calculate percentage of males

percentage_female = (women / total_students) * 100 #Calculate percentage of females

#Outputs

print(f"There are {total_students} students in the sports department, of which {percentage_male:.2f}% are male and {percentage_female:.2f}% are female.")
