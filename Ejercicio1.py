#KevMJ
"""Programa para dar un descuento si la compra del cliente es mayor a $2500"""

monto_compra = float(input("¿Cuál es el monto de compra? "))
monto_minimo_descuento = 2500.0
porcentaje_descuento = 8.0

# Condicion para aplicar descuento 
if monto_compra > monto_minimo_descuento:
    a_pagar = monto_compra * (1-(porcentaje_descuento/100))
else:
    a_pagar = monto_compra
  
print(f"Lo que el cliente debe es: {a_pagar}")


"""Actividad 3
Indicaciones:

Desarrolla un algoritmo para calcular el precio de venta de un articulo. Se tiene como datos, la descripción del articulo y el costo de producción, el precio de venta se calcula añadiéndole el costo de producción del 120% como utilidad 
y el 15% de impuesto de fabricación. Se imprimirá la descripción del articulo y el precio de venta.

Requisitos para la actividad:
Realizar lo solo con la estructura condicional IF
Los datos son ingresados por el usuario
El código debe ser legible y descriptivo (añadir comentarios si es necesario)"""


detalle_articulo = input("Descripción del artículo: ")
costo_de_produccion = input("Ingresa el costo de producción: ")

precio_venta = costo_de_produccion * 1.2 + costo_de_produccion * 0.15

print(f"El artìculo {detalle_articulo}" + f" tendra un precio de venta de: {precio_venta}")



