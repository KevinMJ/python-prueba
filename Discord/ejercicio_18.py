"""
Ejercicio python_desde_cero_2024
Programmer: KevMJ

!Desarrolla un algoritmo que calcule el desglose en billetes y monedas de una cantidad exacta en pesos mexicanos. Hay billetes de 500, 200, 100, 50, 20 y monedas de 10, 5, 2 y 1.
!Por ejemplo, si deseamos conocer el desglose de $434, el programa mostrara por pantalla el siguiente resultado:
? 2 billetes de 200 pesos.
? 1 billete de 20 pesos.
? 1 billete de 10 pesos.
? 2 monedas de 2 pesos.
"""

#Inputs
cash = int(input("type in the amount of money you want to break down: "))

bills_500 = 0
bills_200 = 0
bills_100 = 0
bills_50 = 0
bills_20 = 0

coins_10 = 0
coins_2 = 0
coins_1 = 0


# Program
if cash > 500:
    bills_500 = int(cash / 500)
    cash = cash % 500

if cash > 200:
    bills_200 = int(cash / 200)
    cash = cash % 200

if cash > 100:
    bills_100 = int(cash / 100)
    cash = cash % 100

if cash > 50:
    bills_50 = int(cash / 50)
    cash = cash % 50


if cash > 20:
    bills_20 = int(cash / 20)
    cash = cash % 20

if cash > 10:
    coins_10 = int(cash / 10)
    cash = cash % 10

if cash > 5:
    coins_10 = int(cash / 5)
    cash = cash % 5

if cash > 2:
    coins_2 = int(cash / 2)
    coins_1 = int(cash % 2)

#Outputs

print(f"Your money could be break down into {bills_500:.0f} bills of $500, {bills_200:.0f} bills of $200, {bills_100:.0f} bills of $100,{bills_50:.0f} bills of $50, {bills_20:.0f} bills of $20, {coins_10:.0f} coins of 10, {coins_2:.0f} coins of 2, {coins_1:.0f} coins of 1")