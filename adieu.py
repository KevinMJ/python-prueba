
def main():

    name = []
    j = 0
    while True:
        try:
            name.append(input("Name: ")) 
        except EOFError:
            print("\nAdieu, adieu to ", end="")
            while True:
                if len(name) == 1:
                    print(name[0])
                    break
                    
                if len(name) == 2:
                    print(name[0],"and", name[1])
                    break
                
                if len(name) > 2:
                    print(name[0],",",end="")
                    name.pop(0)


if __name__ == "__main__":
    main()