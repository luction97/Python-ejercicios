# 12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro 
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día 
# ingresado no es ninguno de esos, imprimir otro mensaje. 

def obtener_mensaje(dia):
    dia = dia.lower().strip()
    if dia == "lunes":
        return "Es lunes, pasear el perro."
    elif dia == "viernes":
        return "Es viernes, entregar trabajo práctico de programación."
    elif dia == "sábado" or dia == "domingo":
        return "Es fin de semana, estudiar y descansar."
    else:
        return "A seguir trabajando!"



dia = input("Ingrese un día de la semana: ").strip()

# Imprimir el mensaje correspondiente
print(obtener_mensaje(dia))


