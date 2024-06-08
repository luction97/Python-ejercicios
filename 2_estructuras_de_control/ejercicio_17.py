# 17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos_hasta_100():
    contador_primos = 0
    primos = []

    for num in range(101):
        if es_primo(num):
            primos.append(num)
            contador_primos += 1

    print("Números primos entre 0 y 100:")
    print(primos)
    print(f"Total de números primos: {contador_primos}")


mostrar_primos_hasta_100()