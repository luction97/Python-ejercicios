# 3. Que nos calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%. 


def totalConIVA(total, iva=21):
    return total + (total * iva) / 100


total = float(input("Ingresa el total sin IVA: "))
porcentaje_iva = float(input("Ingresa el porcentaje de IVA (opcional), sino presiona enter para continuar con 21% por defecto.  "))
100
print(f"Total con IVA: {totalConIVA(total, porcentaje_iva)}")