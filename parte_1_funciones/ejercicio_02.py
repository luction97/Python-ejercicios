# Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado. 



def calcularPotencia(num1,numElevar):
    if num1 > 0:
     return num1**numElevar
    else:
        return None

print(calcularPotencia(-3,3))