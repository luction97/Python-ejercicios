from operator import index

#  Dada la siguiente lista:
paises = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]
print("Lista de paises: ", paises,"\n")

#  realizar lo siguiente:



# A. Imprimir la cantidad de elementos que tiene la lista.
print("Cantidad de elementos: ", len(paises),"\n")



# B. Imprimir el primer y último elemento.
print("Primer elemento: ",paises[0], "\nÚltimo elemento: ",paises[-1],"\n")



# C. Imprimir el resto.
print("Resto de los elementos: ", paises[1:-1],"\n")



# D. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
# la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.

rta_user = input("Ingrese el nombre de un país para verificar en qué índice se encuentra de la lista:\n").capitalize()

if rta_user in paises:
    print(f"El país {rta_user} se encuentra en el índice ", paises.index(rta_user),"\n")
else: 
    print(f"El país {rta_user} no se encuentra en la lista\n")



#  E. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#  la lista. Quitar el elemento correspondiente de esa posición.

print("Cantidad de elementos actualmente en la lista: ", len(paises),"\n")
num_user = int(input("Ingrese un número igual o menor a la cantidad de elementos de la lista para quitarlo.\n"))

if 0 <= num_user < len(paises):
    elimina_pais = paises.pop(num_user)
    print(f"{elimina_pais} eliminado. \n")
else:
    print("El número ingresado no es válido.\n")

print(f"Lista actual:{paises}")



#  F.  Imprimir la lista en orden inverso.
paises.reverse()
print("Lista al revés: \n",paises,"\n")



# G. Vaciar la lista.
paises.clear()
print("Lista vaciada.\n", paises)