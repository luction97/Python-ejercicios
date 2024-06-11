#  6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
#  de una lista vacía:
#  a. Agregar un elemento al final.
#  b. Agregar un elemento al principio.
#  c. Quitar un elemento al final.
#  d. Quitar un elemento al principio.


def mostrarMenu():
    print("\nOpciones:")
    print("1. Agregar un elemento al final")
    print("2. Agregar un elemento al principio")
    print("3. Quitar un elemento al final")
    print("4. Quitar un elemento al principio")
    print("5. Salir")

def agregarAlFinal(lista, elemento):
    lista.append(elemento)

def agregarAlPrincipio(lista, elemento):
    lista.insert(0, elemento)

def eliminaDelFinal(lista):
    if lista:
        return lista.pop()
    else:
        print("La lista está vacía, no se puede quitar un elemento.")
        return None

def eliminaDelPrincipio(lista):
    if lista:
        return lista.pop(0)
    else:
        print("La lista está vacía, no se puede quitar un elemento.")
        return None

lista_vacia = []
while True:
    mostrarMenu()
    opcion = input("Elija una opción: ")
    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar al final: ")
        agregarAlFinal(lista_vacia, elemento)
    elif opcion == "2":
        elemento = input("Ingrese el elemento a agregar al principio: ")
        agregarAlPrincipio(lista_vacia, elemento)
    elif opcion == "3":
        elemento = eliminaDelFinal(lista_vacia)
        if elemento is not None:
            print(f"Elemento quitado del final: {elemento}")
    elif opcion == "4":
        elemento = eliminaDelPrincipio(lista_vacia)
        if elemento is not None:
            print(f"Elemento quitado del principio: {elemento}")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
    
    print(f"Lista actual: {lista_vacia}")
