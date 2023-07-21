# Función para calcular una serie repetida a partir de un número dado y una cantidad de términos
def serie_repetida(numero, terminos):
    suma_total = 0  # Variable para almacenar la suma total de los términos de la serie
    termino_actual = 0  # Variable para mantener el término actual de la serie

    for i in range(terminos):
        termino_actual = (
            termino_actual * 10 + numero
        )  # Cálculo del término actual de la serie
        suma_total += termino_actual  # Agregar el término actual a la suma total

    return suma_total  # Devolver la suma total de los términos de la serie


# Ejemplo 1: Calcular una serie repetida con el número 3 y 5 términos
print(serie_repetida(3, 5))

# Ejemplo 2: Calcular una serie repetida con el número 5 y 3 términos
print(serie_repetida(5, 3))
