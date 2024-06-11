
# Funciones

def crearListaNumerica(): # Crea una lista con números ingresados por teclado
    salir = False
    lista_numeros = []
    while salir == False:
        rta_user = input("Ingresa un número o 'fin' para terminar. \n")

        if rta_user.lower() == 'fin':
            salir = True
        else:
            lista_numeros.append(int(rta_user))     
    print("Su lista de números:", lista_numeros)
    return lista_numeros


def numeroMaximo(lista): # A. Obtiene el número máximo de la lista ingresada
    if lista_numeros is not None:
       return max(lista_numeros)
    else:
        print("La lista está vacía.")


def segundoNumeroMaximo(lista_numeros): # B. Obtiene el segundo mayor número de la lista
   lista_ordenada = sorted(lista_numeros)
   return lista_ordenada[-2]


def numeroMinimo(lista): # C. Obtiene el número máximo de la lista ingresada
    if lista_numeros is not None:
       return min(lista_numeros)
    else:
        print("La lista está vacía.")


def multiplicacionDeNumeros(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def contarParesEImpares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = len(lista) - pares
    return pares, impares

def removerRepetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

#  5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
#  usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  Cada uno
#  de los números ingresados por el usuario deberá ser almacenado en una lista. 



# A continuación, realice las siguientes tareas:

#  a. Determinar el máximo.

lista_numeros = crearListaNumerica()
numero_maximo = numeroMaximo(lista_numeros)
print(f"El número máximo ingresado es [{numero_maximo}]")


#  b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.

segundo_maximo = segundoNumeroMaximo(lista_numeros)
print(f"El segúndo valor máximo es [{segundo_maximo}]")


#  c. Determinar el mínimo.
numero_minimo = numeroMinimo(lista_numeros)
print(f"El número mínimo ingresado es [{numero_minimo}]")

#  d. Calcular la multiplicación de  todos los números de la lista.

multiplicacion_lista = multiplicacionDeNumeros(lista_numeros)
print(f"El resultado de multiplicar todos los números de la lista es {multiplicacion_lista}")


#  e. Contar los valores pares e impares.
pares, impares = contarParesEImpares(lista_numeros)
print(f"Números pares: {pares}\n Números impares: {impares}")


#  f. Remover los elementos repetidos.

lista_sin_repetidos = removerRepetidos(lista_numeros)
print(f"Lista antes: {lista_numeros}")
print(f"Lista ahora, sin repetidos: {lista_sin_repetidos}")