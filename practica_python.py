frase = ["Estoy", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "dias", "de", "Programación", "Fácil"]

print(" ".join(frase))

"""------------------------------------------------------------------"""

colores = ["rojo", "azul", "verde", "amarillo"]
GUION = "-"
PUNTO = "."

for color in colores:
    print("{} {}{}".format(GUION, color.capitalize(), PUNTO))


"""------------------------------------------------------------------"""

numero_1 = 10
numero_2 = 34.50

resultado = numero_1 * numero_2

print(f"La multiplicación de %i * %.2f da como resultado: %.2f" % (numero_1, numero_2, resultado))

"""------------------------------------------------------------------"""

texto = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas"

contador = 0
letra_a_encontrar = input("Ingresa la letra a buscar: ")

for letra in texto:
    if letra == letra_a_encontrar:
        contador += 1
    else:
        pass
print("El número de ocurrencias de %s es de %i" % (letra_a_encontrar, contador))

"""------------------------------------------------------------------"""
