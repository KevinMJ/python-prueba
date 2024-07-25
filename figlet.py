from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    list = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(list))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font = sys.argv[2])
        else:
            print("Por favor, proporciona el comando -f o --font antes de escribir la fuente deseada.")
            sys.exit(1)
    else:
        print("Por favor, proporciona el comando -f o --font antes de escribir la fuente deseada y al menos una fuente")
        sys.exit(1)

    prompt = input("Input: ")
    print(figlet.renderText(prompt))

if __name__ == "__main__":
    main()