
def suma(a, b):
    return a+b
def resta(a, b):
    return a-b 
def multi(a, b):
    return a*b
def divi(a, b):
    return a/b


def operacion():

    a = float(input("Ingresa el valor de a: \n"))
    b = float(input("Ingresa el valor de b: \n"))

    desicion = input("Que operacion quieres hacer (S/R/M/D): \n").upper()

    try:
        if desicion == "S":
            print(suma(a,b))
        elif desicion == "R":
            print(resta(a, b))
        elif desicion == "M":
            print(multi(a, b))
        elif desicion == "D":
            print(divi(a, b))

    except ZeroDivisionError:
        print("No se puede procesar una division sobre 0")

if __name__ == "__main__":
    operacion()