# Función para filtrar números en una lista de entrada
def filtrar_numeros(lista_entrada):
    lista_salida = []  # Se crea una lista vacía para almacenar los números filtrados.

    for num in lista_entrada:
        # Si el número es mayor que 1000, se devuelve la lista actual sin procesar más elementos.
        if num > 1000:
            return lista_salida

        # Si el número es mayor que 600, se ignora y se pasa al siguiente elemento.
        if num > 600:
            continue

        # Si el número es divisible por 5, se agrega a la lista de salida.
        if num % 5 == 0:
            lista_salida.append(num)

    return lista_salida  # Se devuelve la lista filtrada.


# Ejemplo de entrada1 y salida1
entrada1 = [24, 150, 300, 660, 295, 1050, 50]
salida1 = filtrar_numeros(entrada1)
print(salida1)

# Ejemplo de entrada2 y salida2
entrada2 = [110, 720, 307, 555, 1095, 12, 300, 1000]
salida2 = filtrar_numeros(entrada2)
print(salida2)
