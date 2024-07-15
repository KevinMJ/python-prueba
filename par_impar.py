# Lo primero que realizamos es dar la bienvenida y preguntar por un número entre 1 y 1000
print("Bienvenido, ganarás si escribes un número par")
def main():
	numero = int(input("Ingresa un número entre 1 y 1000: "))
	par_impar(numero)
def par_impar(numero):
	if numero%2 == 0:
		print("Es un número par, FELICIDADES")
		return
	else:
		print("intenta nuevamente")
		main()
main()

