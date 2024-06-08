# 2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado. 


def calcularPotencia(num,potencia):
    if num > 0:
     return num**potencia
    else:
        return None

num = int(input("ingresa el primer número entero positivo"))
potencia = int(input("Ingresa una potencia a elevar"))

print(calcularPotencia(num,potencia))