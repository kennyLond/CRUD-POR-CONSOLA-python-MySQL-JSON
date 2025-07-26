import  json
import os

personas= []

def cargar_datos():
    global personas
    if os.path.exists("personas.json"):
        with open("personas.json", "r") as archivo:
            try:
                personas = json.load(archivo)
            except json.JSONDecodeError:
                personas = []
    else:
        personas = []

def guardar_datos():
    with open("personas.json", "w") as archivo:
        json.dump(personas, archivo, indent=4)

def registrar_persona():
    nombre = input ("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")

    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    personas.append(persona)
    guardar_datos()
    print("La persona ha sido guardada con exito")

def mostrar_persona():
    if not personas:
        print("no hay personas registradas")
    else:
        for p in personas:
            print(f"{p['nombre']},{p['edad']},{p['ciudad']}")
            
def buscar_persona():
    nombre_buscado = input("Ingesa el nombre a buscar")
    for p in personas:
        if p["nombre"].lower() == nombre_buscado.lower():
            print(f"Encontrado: {p['nombre']},{p['edad']},{p['ciudad']}")
            return
    print("Persona no encontrada")

def borrar_persona():
    nombre_borrar = input("Ingrese el nombre a eliminar")
    for p in personas:
        if p["nombre"].lower() == nombre_borrar.lower():
            personas.remove(p)
            guardar_datos()
            print("Persona eliminada")
            return
    print("Persona no encontrada")