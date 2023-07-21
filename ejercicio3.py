# Función para agrupar elementos similares en una lista
def agrupar_elementos_similares(lista):
    diccionario = (
        {}
    )  # Se crea un diccionario vacío para almacenar los elementos similares.

    for elemento in lista:
        if elemento in diccionario:
            # Si el elemento ya está en el diccionario, se agrega a su lista correspondiente.
            diccionario[elemento].append(elemento)
        else:
            # Si el elemento no está en el diccionario, se crea una nueva lista con el elemento.
            diccionario[elemento] = [elemento]

    lista_salida = list(
        diccionario.values()
    )  # Se obtiene una lista con los valores del diccionario.

    return lista_salida  # Se devuelve la lista con los elementos similares agrupados.


# Ejemplo de entrada1 y entrada2
entrada1 = [12, 25, 1, 1, 7, 25]
entrada2 = [6, 7, 8, 9]

# Se llama a la función agrupar_elementos_similares con las entradas y se imprime el resultado.
print(agrupar_elementos_similares(entrada1))
print(agrupar_elementos_similares(entrada2))
