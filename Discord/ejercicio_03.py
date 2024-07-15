"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

Actividad 3
Indicaciones:

Desarrolla un algoritmo para calcular el precio de venta de un articulo. 
Se tiene como datos, la descripción del articulo y el costo de producción, 
el precio de venta se calcula añadiéndole el costo de producción del 120% como utilidad 
y el 15% de impuesto de fabricación. Se imprimirá la descripción del articulo y el precio de venta.

Requisitos para la actividad:
Realizar lo solo con la estructura condicional IF
Los datos son ingresados por el usuario
El código debe ser legible y descriptivo (añadir comentarios si es necesario)"""


article_description = input("Enter article description: ")
production_cost = float(input("Which is the production cost? "))
selling_price = production_cost * (2.2 + 0.15)

print(f"The article {article_description} should have a slling price of: {selling_price:.2f}")
