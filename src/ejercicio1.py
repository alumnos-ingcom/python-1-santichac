################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados
fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura
en grados centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados
centígrados y retorne el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrenheit(centigrados):
    """Esta funcion sirve para cambiar de
    centigrados a fahrenheit"""
    return (centigrados * 9/5) + 32

def convertir_a_centigrados(fahrenheit):
    """Esta funcion sirve para cambiar de
    centigrados a fahrenheit"""
    return (fahrenheit - 32) * 5/9

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    grados_c = float(input('Introcuzca los grados centigrados para convertir a fahrenheit:'))
    conversion_centigrados = convertir_a_fahrenheit(grados_c)

    print(conversion_centigrados)

    grados_f = float(input('Introduzca los grados fahrenheit para convertir a centigrados:'))
    conversion_fahrenheit = convertir_a_centigrados(grados_f)

    print(conversion_fahrenheit)

if __name__ == "__main__":
    principal()

