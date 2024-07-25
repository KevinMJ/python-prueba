"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ


!Una compañía de taxis cobra una tarifa base de $50.00, más una tarifa por kilómetro recorrido y una tarifa adicional por tráfico pesado. Las tarifas son las siguientes:

!    $10.00 por kilómetro si la distancia es menor a 10 km.
!    $8.00 por kilómetro si la distancia está entre 10 km y 50 km.
!    $5.00 por kilómetro si la distancia es mayor a 50 km.
!    Se añade una tarifa adicional de $20.00 si el tráfico es pesado.

!Desarrolla un algoritmo que calcule e
>>>imprima el costo total del viaje en taxi.
"""

#Inputs
distance = float(input("How many kilometers did your vehicle travel? "))
heavy_traffic = input("Is the traffic heavy? Yes/No ")

# Program

if distance < 10:
    total_cost = 10 * distance
elif 10 <= distance < 50:
    total_cost = 8 * distance
elif 50 <= distance:
    total_cost = 5 * distance

if heavy_traffic == "Yes":
    total_cost += 20

print(f"The total cost for {distance} kilometers is ${total_cost:.2f}")