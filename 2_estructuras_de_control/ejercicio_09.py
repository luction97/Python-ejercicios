# 9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso 
# en que ambos números son iguales.




#1. Ingresan dos numeros por el usuario
# ingrese un numero


def verificarMenorNum(num1, num2):
    if(num1 < num2):
     print(str(num1)+" es menor que "+str(num2))
    elif(num2 < num1):
     print(str(num2)+" es menor que "+str(num1))
    elif(num2 == num1):
     print("Ambos números son iguales")


print("Ingresará dos números para verificar cuál es menor, o si son iguales.")
num1 = int(input("Ingrese el primer número: \n"))
num2 = int(input("Ingrese el segundo número: \n"))

verificarMenorNum(num1,num2)
