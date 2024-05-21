# 10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente: 
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas. 
# c. Que indique si es primo o no. 
# d. Por último, su factorial.


# FUNCIONES:
def imparesHasta(num):
    if(num > 0): # Verifica que el número entero sea positivo
     for i in range(1, num+1):
        if i % 2 != 0:
            print(i, end=", ")
    else:
       print("Debes ingresar un número entero positivo.")



def cuentaAtras(num):
    for i in range(num, -1, -1):
       print(i, end=", ")


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)



# PROGRAMA:
num = int(input("Ingrese un número entero positivo: \n"))

# a. Todos los números impares desde 1 hasta ese número separados por comas.
print("Estos son todos los números impares desde 1 hasta ",num)
imparesHasta(num)
print("\n")


# b. La cuenta atrás desde ese número hasta cero separados por comas. 
print("Esta es la cuenta atrás del número ",num," hasta cero.")
cuentaAtras(num)
print("\n")


# c. Que indique si es primo o no. 
if(es_primo(num)):
   print("El número: ",num," es un número primo. \n")
else:
   print("No es un número primo. \n")


# d. Su factorial.
print(f"El factorial de {num} es: {factorial(num)} \n")


