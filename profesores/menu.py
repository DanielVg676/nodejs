import os
import requests

URLbase = "http://localhost:5000"

def listar_profesores():
    response = requests.get(f"{URLbase}/profesores")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error al listar profesores")

def buscar_profesor(entrada):
    response = None
    if entrada.isdigit():
        response = requests.get(f"{URLbase}/profesor/{entrada}")
    else:
        response = requests.get(f"{URLbase}/profesor/nombre/{entrada}")
    
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error al buscar profesor")


def registrar_profesor(id, nombre, correo, direccion):
    data = {
        "id": id,
        "nombre": nombre,
        "correo": correo,
        "direccion": direccion
    }
    response = requests.post(f"{URLbase}/profesor/registrar", json=data)
    if response.status_code == 200:
        print("Profesor registrado")
    else:
        print("Error al registrar profesor")

def modificar_profesor(id, nombre, correo, direccion):
    data = {
        "id": id, 
        "nombre": nombre,
        "correo": correo,
        "direccion": direccion
    }
    response = requests.put(f"{URLbase}/profesor/modificar", json=data)
    if response.status_code == 200:
        print("Profesor modificado")
    else:
        print("Error al modificar profesor")

def eliminar_profesor(id):
    response = requests.delete(f"{URLbase}/profesor/eliminar/{id}")
    if response.status_code == 200:
        print("Profesor eliminado")
    else:
        print("Error al eliminar profesor")

def menu():
    while True:
        print("...::: MENU DE OPCIONES PARA SISTEMA DE PROFESORES :::...")
        print("1. Listar profesores")
        print("2. Obtener profesor")
        print("3. Registrar profesor")
        print("4. Modificar profesor")
        print("5. Eliminar profesor")
        print("6. Salir")
        opcion=input("Ingrese el numero de la accion que desee realizar: ")

        if opcion == '1':
            os.system("cls")
            listar_profesores()
        elif opcion == '2':
            os.system("cls")
            id = input('Ingrese el ID del profesor: ')
            os.system("cls")

            buscar_profesor(id)
        elif opcion == '3':
            os.system("cls")
            id = input('Ingrese el ID del profesor: ')
            nombre = input('Ingrese el nombre del profesor: ')
            correo = input('Ingrese el correo del profesor: ')
            direccion = input('Ingrese la dirección del profesor: ')
            os.system("cls")

            registrar_profesor(id, nombre, correo, direccion)
        elif opcion == '4':
            os.system("cls")
            id = input('Ingrese el ID del profesor: ')
            nombre = input('Ingrese el nuevo nombre del profesor: ')
            correo = input('Ingrese el nuevo correo del profesor: ')
            direccion = input('Ingrese la nueva dirección del profesor: ')
            os.system("cls")

            modificar_profesor(id, nombre, correo, direccion)
        elif opcion == '5':
            id = input('Ingrese el ID del profesor: ')
            
            eliminar_profesor(id)
        elif opcion == '6':
            os.system("cls")
            print("Salienedo del sistma......")
            break
        else:
            os.system("cls")
            print('Opción no válida')

menu()