# 6.  Que pida al usuario una palabra y la muestre por pantalla 10 veces.

def mostrarPalabra():
    palabra = input("Ingrese una palabra para mostrarla 10 veces.\n")
    for i in range(10):
     print(f"{i+1}. "+palabra)

    
mostrarPalabra()
