#  Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#  Imprimir por pantalla el resultado.

# Funcion

def ordenarNumeros(lista):
    lista_num_str = num_user.split(',') # almaceno una lista de números tipo string
    for i in lista_num_str: 
        num  = int(i) # Itero cada número convirtiendolo a int
        lista.append(num)  # Agrego los números de tipo int a la lista final.

    lista.sort() #Ordeno los números
    return lista  



# Programa

lista_numeros = []
num_user = input("Ingrese 5 números separados por coma, ejemplo: '1,2,3' \n")
ordenarNumeros(lista_numeros)
print(lista_numeros)

