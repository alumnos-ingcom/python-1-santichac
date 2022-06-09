################
# Santiago Julián Chacón - @santicahc
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero
entero positivo y negativo.
"""

def division_lenta(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        cociente += 1
        dividendo = dividendo - divisor
    return (f'El cociente es {cociente} y el resto es {dividendo}')

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input('Ingrese un número para dividir: '))
    divisor = int(input('Ingrese el número por el cual lo quiera dividir: '))
    print(division_lenta(dividendo, divisor))

if __name__ == "__main__":
    principal()

