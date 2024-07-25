import inflect

p = inflect.engine()

def main():

    while True:

        try:
            x = input("Input: ")
            mylist = p.join(x, final_sep="")
        
        except EOFError:
            print("\nAdieu, adieu to ", end="")
            print(mylist)

if __name__ == "__main__":
    main()