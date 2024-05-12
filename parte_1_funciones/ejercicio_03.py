# 3. Que nos calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%. 


def totalConIVA(total, iva=21):
    return total + (total * iva) / 100


print(totalConIVA(100))
