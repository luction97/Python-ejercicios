# Que dado tres números ingresados por el usuario nos devuelva el promedio. 
# El usuario ingresa 3 numeros
# esos numeros se suman y se divide por la cantidad (3)
# devuelve el promedio

def calcularPromedio(num1,num2,num3):
    return ( num1+num2+num3) / 3

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))    
promedio = calcularPromedio(num1, num2, num3)
        
print(f"El promedio de los números ingresados es: {promedio}")

