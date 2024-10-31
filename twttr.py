def main():
    shorten(input("Input: "))

def shorten(word):
    vocals = ("a","e","i","o","u","A","E","I","O","U")
    for letter in word:
        for vocal in vocals:
            count = 0
            if letter == vocal:
                count += 1
            word = word.replace(vocal, "", count)
    return f"{word}"

if __name__ == "__main__":
    main()