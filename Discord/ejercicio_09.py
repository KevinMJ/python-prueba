"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!El promedio de practicas de un curso se calcula en base a cuatro practicas calificadas de las cuales se elimina la calificación menor, y se promedian las tres restantes. Desarrolla un algoritmo que calcule e 
>>> imprima el promedio de las practicas de un estudiante y la calificación menor.
"""

# Inputs 
grade_1 = float(input("Enter the grade of the practice 1: "))
grade_2 = float(input("Enter the grade of the practice 2: "))
grade_3 = float(input("Enter the grade of the practice 3: "))
grade_4 = float(input("Enter the grade of the practice 4: "))

# Program 

if grade_1 < grade_2:
    if grade_1 < grade_3:
        if grade_1 < grade_4:
            lower = grade_1
        else:
            lower = grade_4
    else:
        if grade_3 < grade_4:
            lower = grade_3
        else:
            lower = grade_4    
else:
    if grade_2 < grade_3:
        if grade_2 < grade_4:
            lower = grade_2
        else:
            lower = grade_4
    else:
        if grade_3 < grade_4:
           lower = grade_3
        else:
           lower = grade_4
           
average_practices = (grade_1+grade_2+grade_3+grade_4-lower)/3


# Outputs 
print(f"The average practices per student are {average_practices:.2f} and the lowest grade is: {lower}")