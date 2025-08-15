from queue import PriorityQueue
def quick_sort_nombre(lista):#Funcion para ordenar nombre de A/Z
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["nombre"].lower() <= pivote["nombre"].lower()]
        mayores = [x for x in lista[1:] if x["nombre"].lower() > pivote["nombre"].lower()]
        return quick_sort_nombre(menores) + [pivote] + quick_sort_nombre(mayores)

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
            dorsal = input("Ingrese número del dorsal del participante: ").strip()
            if not dorsal.isdigit():
                print("El dorsal debe contener solo números.")
            elif any(p["dorsal"] == dorsal for p in participantes):
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
                    print("La edad debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        while True:
            categoria = input("Ingrese la categoría (juvenil, adulto, master): ").strip()
            if not categoria:
                print("La categoría no puede estar vacía.")
            else:
                break

        participantes.append({
            "dorsal": dorsal,
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        })

def mostrar_por_nombre(participantes):
    ordenados = quick_sort_nombre(participantes)
    print("\n--- Participantes ordenados por nombre (A-Z) ---")
    for p in ordenados:
        print(f"Dorsal: {p['dorsal']} | Nombre: {p['nombre']} | Edad: {p['edad']} | Categoría: {p['categoria']}")

def mostrar_por_edad(participantes):
    ordenados = sorted(participantes, key=lambda p: p["edad"])
    print("\n--- Participantes ordenados por edad (menor a mayor) ---")
    for p in ordenados:
        print(f"Dorsal: {p['dorsal']} | Nombre: {p['nombre']} | Edad: {p['edad']} | Categoría: {p['categoria']}")

def menu():
    participantes = []  # Lista de diccionarios
    while True:
        print("\n**** Menú ****")
        print("1. Ingreso de participantes")
        print("2. Participantes ordenados por nombre")
        print("3. Participantes ordenados por edad")
        print("4. Salir")

        opcion = input("Ingrese una opción: ").strip()

        match opcion:
            case "1":
                ingreso_participante(participantes)
            case "2":
                mostrar_por_nombre(participantes)
            case "3":
                mostrar_por_edad(participantes)
            case "4":
                print("Salir...")
                break
            case _:
                print("Opción inválida...")

menu()
