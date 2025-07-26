from funciones import *


cargar_datos()


def mostrar_menu():
    print("\n-- Menú --")
    print("1. Registrar persona")
    print("2. Mostrar personas")
    print("3. Buscar persona")
    print("4. Eliminar persona")
    print("5. Salir")


while True:
    mostrar_menu()  
    opcion = input("Selecciona una opción: ")

    
    if opcion == "1":
        registrar_persona()
    elif opcion == "2":
        mostrar_persona()
    elif opcion == "3":
        buscar_persona()
    elif opcion == "4":
        borrar_persona()
    elif opcion == "5":
        print("Ha salido del sistema.")
        break  # Salimos del while
    else:
        print("Opción no válida. Intenta de nuevo.")
