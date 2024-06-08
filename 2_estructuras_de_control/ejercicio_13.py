# 13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos 
# A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un 
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el 
# resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla 
# el grupo que le corresponde. 


def identificarGrupo(nombre, sexo):
    # Mujeres con nombre anterior a 'M'                                                              # Hombres con nombre posterior a la letra 'N'
    if nombre and (nombre[0].lower() < 'm' and (sexo.lower() == 'mujer' or sexo.lower() == 'm')) or (nombre[0].lower() > 'n' and (sexo.lower() == 'hombre' or sexo.lower() == 'h')):
        return "Le corresponde: -> Grupo A"
    else:
        return "Le corresponde: -> Grupo B"
    




# Preguntar al usuario nombre y sexo.  
nombre = input("Ingrese su nombre \n")
sexo = input("Ingrese su sexo \n")

# Mostrar en pantalla el grupo al que corresponde
print(identificarGrupo(nombre, sexo))


