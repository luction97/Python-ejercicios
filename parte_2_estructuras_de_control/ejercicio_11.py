# 11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se 
# encuentran en dicha frase. 


def contarVocales(frase):
        cantidad_vocales = 0
        vocales = "aeiouAEIOU"
        for caracter in frase:
             if caracter in vocales:
                cantidad_vocales += 1
        return cantidad_vocales



frase = input("Ingrese una frase para contar sus vocales. \n")
print(f"La frase contiene {contarVocales(frase)} vocales")
