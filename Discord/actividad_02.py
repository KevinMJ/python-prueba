"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!En un negocio de productos electrodomésticos se aplica un descuento 
del 8% a todos los clientes cuya compra sea mayor a $2500. 
Teniendo como dato el monto de la compra del cliente.
>>>imprime lo que debe el cliente.
"""

ticket_price = float(input("ticket amount? "))

# Conditional to check if the client deserve a discount 
if ticket_price > 2500:
    to_pay = ticket_price * 0.92
else:
    to_pay = ticket_price
  
print(f"Total to pay: {to_pay}")

