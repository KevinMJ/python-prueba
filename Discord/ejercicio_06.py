"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Dado un numero entero de tres cifras, desarrolla un algoritmo para verificar que efectivamente sean 3 cifras e invertir el numero de entrada.
>>>Imprime el numero invertido
?Restricciones:
- No utilizar listas ni tuplas
- No utilizar funciones built-in, ni módulos
- Solo utiliza procesos lógicos y matemáticos
"""
# Asking for three digit number
three_digit_whole_number = int(input("type in three-digit whole number "))


if three_digit_whole_number < 1000: # Conditional to check if is three-digit whole number 
    first_digit = 0
    second_digit = 0
    third_digit = 0

    # Conditionals to check which is the first_digit in the number provided, checking ranges in hundreds----
    if 900 < three_digit_whole_number < 999:
        first_digit = 9
        second_digit_reference = three_digit_whole_number - 900 # In order to get a reference to find the next two digits, we need to subtract the hundreds
    elif 800 <three_digit_whole_number < 899:
        first_digit = 8
        second_digit_reference = three_digit_whole_number - 800
    elif 700 <three_digit_whole_number < 799:
        first_digit = 7
        second_digit_reference = three_digit_whole_number - 700
    elif 600 <three_digit_whole_number < 699:
        first_digit = 6
        second_digit_reference = three_digit_whole_number - 600
    elif 500 <three_digit_whole_number < 599:
        first_digit = 5
        second_digit_reference = three_digit_whole_number - 500
    elif 400 <three_digit_whole_number < 499:
        first_digit = 4
        second_digit_reference = three_digit_whole_number - 400
    elif 300 <three_digit_whole_number < 399:
        first_digit = 3
        second_digit_reference = three_digit_whole_number - 300
    elif 200 <three_digit_whole_number < 299:
        first_digit = 2
        second_digit_reference = three_digit_whole_number - 200
    elif 100 <three_digit_whole_number < 199:
        first_digit = 1
        second_digit_reference = three_digit_whole_number - 100
    else:
        first_digit = 0
    #-----

    #Conditionals to get the second and the third digit in the number provided, checking ranges in tens---

    if 90 < second_digit_reference < 99:
        second_digit = 9
        third_digit = second_digit_reference - 90 # If we substract the tens from the reference we get the last digit

    elif 80 < second_digit_reference < 89:
        second_digit = 8
        third_digit = second_digit_reference - 80

    elif 70 < second_digit_reference < 79:
        second_digit = 7
        third_digit = second_digit_reference - 70

    elif 60 < second_digit_reference < 69:
        second_digit = 6
        third_digit = second_digit_reference - 60

    elif 50 < second_digit_reference < 59:
        second_digit = 5
        third_digit = second_digit_reference - 50

    elif 40 < second_digit_reference < 49:
        second_digit = 4
        third_digit = second_digit_reference - 40

    elif 30 < second_digit_reference < 39:
        second_digit = 3
        third_digit = second_digit_reference - 30

    elif 20 < second_digit_reference < 29:
        second_digit = 2
        third_digit = second_digit_reference - 20

    elif 10 < second_digit_reference < 19:
        second_digit = 1
        third_digit = second_digit_reference - 10

    else:
        second_digit = 0


#Outputs
print(f"Your number written in reverse is: {third_digit}{second_digit}{first_digit}")