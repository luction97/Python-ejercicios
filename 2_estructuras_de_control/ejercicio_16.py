#16. Que imprima el siguiente patrón:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

def imprimirPatron():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

imprimirPatron()
