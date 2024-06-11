#  7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
#  con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
#  usuario:
#  a. Agregar nuevas tareas pendientes.
#  b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
#  de la lista de pendientes a la de terminadas.
#  Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
#  listas.

def mostrarMenu():
    print("\nOpciones:")
    print("1. Agregar nueva tarea pendiente")
    print("2. Marcar tarea pendiente como terminada")
    print("3. Salir")

def agregarTareaPendiente(listaPendientes):
    tarea = input("Ingrese la nueva tarea pendiente: ")
    listaPendientes.append(tarea)

def marcarTareaComoTerminada(listaPendientes, listaTerminadas):
    if listaPendientes:
        print("\nTareas pendientes:")
        for tarea in listaPendientes:
            print(f"- {tarea}")
        
        tareaATerminar = input("Ingrese el nombre de la tarea a marcar como terminada: ")
        
        if tareaATerminar in listaPendientes:
            listaPendientes.remove(tareaATerminar)
            listaTerminadas.append(tareaATerminar)
            print(f"Tarea '{tareaATerminar}' marcada como terminada.")
        else:
            print("Tarea no encontrada en la lista de pendientes.")
    else:
        print("No hay tareas pendientes para marcar como terminadas.")

def mostrarEstadoListas(listaPendientes, listaTerminadas):
    print("\nEstado actual de las listas:")
    print("Tareas pendientes:")
    if listaPendientes:
        for tarea in listaPendientes:
            print(f"- {tarea}")
    else:
        print("No hay tareas pendientes.")

    print("Tareas terminadas:")
    if listaTerminadas:
        for tarea in listaTerminadas:
            print(f"- {tarea}")
    else:
        print("No hay tareas terminadas.")

tareasPendientes = []
tareasTerminadas = []

while True:
    mostrarMenu()
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        agregarTareaPendiente(tareasPendientes)
    elif opcion == "2":
        marcarTareaComoTerminada(tareasPendientes, tareasTerminadas)
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 3.")
    
    mostrarEstadoListas(tareasPendientes, tareasTerminadas)

