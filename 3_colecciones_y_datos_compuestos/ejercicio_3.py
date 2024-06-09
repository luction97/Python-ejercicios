#  Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
#  frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
#  debajo la misma lista pero sólo con las frutas que añadió el usuario.

lista_frutas = ["banana", "manzana", "pera"]


print("Actualmente tiene ", lista_frutas," en la lista")
rta_user = input("Ingrese 3 frutas más separadas por coma: \n ")
nuevas_frutas = rta_user.split(",")
lista_frutas.extend(nuevas_frutas)


print("lista completa de frutas: \n", lista_frutas)
print("Frutas agregadas por el usuario: ", lista_frutas[3:7])

