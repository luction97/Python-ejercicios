# Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son 
# múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos 
# ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 
# no es bisiesto. 

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Ingrese un año: "))


if es_bisiesto(year):
    print(f"{year} es bisiesto.")
else:
    print(f"{year} no es bisiesto.")