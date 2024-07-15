
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            return input("Date: ")
        
    print(f"{anno:0004}" + "-" + f"{mes:02}" + "-" + f"{dia:02}")
                

main()

"""try:
            mes = int(fecha[0])
            if mes > 12:
                return True

        except ValueError: 
            mesDia = fecha[0].split(" ")
            mes = months.index(mesDia[0])+1 

        try:    
            dia = int(fecha[1])
            if dia > 31:
                return True
        except ValueError:    
            dia = int(mesDia[1].strip(","))

        anno = int(fecha[2])

        return """