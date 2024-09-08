import random

def main():
    number_to_guess = get_num()
    print(number_to_guess)
    number_guess = get_guess()

    while number_guess != number_to_guess:
        if number_guess < number_to_guess:
            print("Too small!")
        elif number_guess > number_to_guess:
            print("Too large!")
        number_guess = get_guess()

    print("Just right!")

def get_num():
    while True:
        try:
            return random.randrange(int(input("level: ")))+1
        except ValueError:
            pass
        except TypeError:
            pass


def get_guess():
    while True:
        try:
            return int(input("Guess: "))
        except ValueError:
            pass
        except TypeError:
            pass


if __name__ == "__main__":
    main()