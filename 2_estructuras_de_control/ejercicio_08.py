# 8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no. 
def esMayorDeEdad(edad):
    if(edad >= 18):
        return "Es mayor de edad"
    else:
        return "Es menor de edad"




edad = int(input("Ingrese su edad en número: \n"))
print(esMayorDeEdad(edad))

