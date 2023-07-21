# Función para mostrar un reporte completo del inventario
def mostrar_reporte_inventario(inventario):
    # Encabezado del reporte
    print("Reporte de Inventario:")
    print("Grupo".ljust(20) + "Nombre".ljust(30) + "Existentes")
    print("-" * 60)

    # Variable para llevar el total de productos en todo el inventario
    total_productos = 0

    # Iterar sobre cada grupo en el inventario
    for grupo, (productos, existencias) in inventario.items():
        # Calcular el total de productos en el grupo
        total_grupo = sum(existencias)
        total_productos += total_grupo

        # Mostrar los productos y existencias del grupo
        for producto, cantidad in zip(productos, existencias):
            print(f"{grupo.ljust(20)}{producto.ljust(30)}{cantidad}")

        # Mostrar el total de productos en el grupo
        print(f"Total en {grupo}: {total_grupo}\n")

    # Mostrar el total de productos en el inventario completo
    print(f"Total de productos en el inventario: {total_productos}\n")


# Función para mostrar los productos y existencias de un grupo específico
def mostrar_grupo(inventario, grupo):
    # Verificar si el grupo existe en el inventario
    if grupo in inventario:
        # Encabezado del reporte para el grupo específico
        print(f"Productos del grupo {grupo}:")
        print("Nombre".ljust(30) + "Existentes")
        print("-----------------------------------------")

        # Obtener los productos y existencias del grupo
        productos, existencias = inventario[grupo]

        # Mostrar los productos y sus existencias
        for producto, cantidad in zip(productos, existencias):
            print(f"{producto.ljust(30)}{cantidad}")

        # Calcular y mostrar el total de productos en el grupo
        total_grupo = sum(existencias)
        print(f"Total en {grupo}: {total_grupo}\n")

    else:
        # Mostrar un mensaje si el grupo no tiene productos registrados
        print("\n")
        print(f"No hay productos registrados en el grupo {grupo}.\n")


# Función para verificar si una cadena no está vacía
def es_str_no_vacio(cadena):
    return isinstance(cadena, str) and len(cadena.strip()) > 0


# Función para verificar si una cadena contiene solo letras (sin espacios)
def contiene_solo_letras(cadena):
    return all(caracter.isalpha() for caracter in cadena)


# Función para solicitar al usuario una cadena sin números y no vacía
def solicitar_cadena_sin_numeros(mensaje):
    while True:
        entrada = input(mensaje)
        if es_str_no_vacio(entrada) and contiene_solo_letras(entrada):
            return entrada
        elif not es_str_no_vacio(entrada):
            print(
                "Error: No has ingresado un valor. Por favor, ingresa un valor no vacío."
            )
        else:
            print(
                "Error: No se aceptan valores numéricos ni caracteres especiales en este campo."
            )


# Función para solicitar y registrar los nombres y apellidos del usuario
def registrar_persona():
    nombres = solicitar_cadena_sin_numeros("Ingresa tus nombres: ")
    apellidos = solicitar_cadena_sin_numeros("Ingresa tus apellidos: ")
    print("\n")
    tituloRegistrarPersona = f"Bienvenido {nombres} {apellidos}"
    print(tituloRegistrarPersona)
    print("-" * len(tituloRegistrarPersona))


# Función para mostrar el menú de opciones
def mostrar_menu():
    tituloMostrarMenu = "Sistema de inventario. Ingrese una opción"
    print(tituloMostrarMenu)
    print("-" * len(tituloMostrarMenu))
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Mostrar productos por grupo")
    print("4. Salir")


# Función para registrar un producto en el inventario
def registrar_producto(inventario, grupo, producto, cantidad):
    if grupo in inventario:
        productos, existencias = inventario[grupo]
        if producto in productos:
            # Actualizar la cantidad del producto si ya existe en el grupo
            index = productos.index(producto)
            existencias[index] += cantidad
        else:
            # Agregar el producto al grupo con su cantidad
            productos.append(producto)
            existencias.append(cantidad)
    else:
        # Crear un nuevo grupo y agregar el producto con su cantidad
        inventario[grupo] = ([producto], [cantidad])


# Función para mostrar el inventario completo
def mostrar_inventario(inventario):
    print("Nombre".ljust(30) + "Existentes")
    print("-----------------------------------------")

    # Iterar sobre cada grupo en el inventario
    for grupo, (productos, existencias) in inventario.items():
        # Mostrar los productos y existencias de cada grupo
        for producto, cantidad in zip(productos, existencias):
            print(f"{producto.ljust(30)}{cantidad}")

    print()  # Salto de línea al final del inventario


if __name__ == "__main__":
    # Diccionario que almacenará los datos del inventario
    inventario = {}

    # Solicitar y registrar los nombres y apellidos del usuario
    registrar_persona()

    while True:
        # Mostrar el menú de opciones y solicitar la elección del usuario
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        # Ejecutar la acción correspondiente según la opción seleccionada
        if opcion == "1":
            grupo = input(
                "Ingrese el grupo del producto (Lacteos, Limpieza, Cereales, Otros): "
            )
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            registrar_producto(inventario, grupo, producto, cantidad)
            print("Producto registrado/actualizado con éxito.\n")

        elif opcion == "2":
            mostrar_reporte_inventario(inventario)

        elif opcion == "3":
            grupo = input(
                "Ingrese el grupo para mostrar (Lacteos, Limpieza, Cereales, Otros): "
            )
            mostrar_grupo(inventario, grupo)

        elif opcion == "4":
            print("Gracias por usar el sistema de inventario. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.\n")
