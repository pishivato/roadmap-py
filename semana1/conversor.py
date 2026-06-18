def Cel(F):
    return ((F-32) *5/9)
def Far(C):
    return ((C*(9/5))+32)

def Conversion():
    
    try:    
        desicion = input("Quieres convertir la temperatura F/C?: \n").upper()
        TEMP = float(input("Ingresa la temperatura a convertir: \n"))

  
        if desicion == "F":     
            print(Far(TEMP))
        elif desicion == "C":
            print(Cel(TEMP))
    except ValueError:
        print("Uups, ah ocurrido un error, inresa un numero valido")


if __name__ == "__main__":
        Conversion()