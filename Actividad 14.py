from queue import PriorityQueue
def ingreso_participante(participantes):
    while True:
        try:
            cantidad = int(input("¿Cuántos participantes desea ingresar?: "))
            if cantidad <= 0:
                print("Debe ingresar al menos 1 participante.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número válido.")
    for i in range(cantidad):
        print(f"\n--- Ingreso de participante #{i + 1} ---")

        while True:
            dorsal = input("Ingrese numero del dorsal del repartidor: ").strip()
            if not dorsal:
                print("El dorsal no puede estar vacío.")
            elif dorsal in participantes:
                print("Este dorsal ya existe. Intente con otro.")
            else:
                break

        while True:
            nombre = input("Ingrese el nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
            else:
                break

        while True:
            try:
                edad = int(input("Ingrese la edad: "))
                if edad < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        while True:
            categoria = input("Ingrese la categoria (juvenil, adulto, master): ").strip()
            if not categoria:
                print("La categoria no puede estar vacía.")
            else:
                break

        participantes[dorsal] = {
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        }

def menu():
    participantes = {}
    while True:
        print("****Menu****")
        print("1. Ingreso de participantes")
        print("2. Participantes ordenados por nombre")
        print("3. Participantes ordenados por edad")
        print("4.Salir")

        opcion = input("Ingrese una opcion: ").strip()

        match opcion:
            case "1":
                ingreso_participante(participantes)
            case "4":
                print("Salir...")
                break
            case _:
                print("Opcion invalida...")

menu()
