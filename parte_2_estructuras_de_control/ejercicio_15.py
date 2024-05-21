# 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe 
# validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
# informarle que no se puede procesar el dato. 


def es_vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if len(letra) == 1:
        if letra.lower() in vocales:
            return True
        else:
            return False
    else:
        print("Error: No se puede procesar el dato.")
        return False


letra = input("Ingrese una letra: ")


if es_vocal(letra):
    print("Es vocal.")