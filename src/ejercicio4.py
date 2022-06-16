################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer
la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def signo(numero):
    """
    Esta función indica si el numero ingresado
    es positivo, negativo o cero.
    Pre: numero es un número entero positivo o negativo.
    Post: la función devuelve 1 si el número es positivo,
    -1 si es negativo y 0 si es 0.
    """
    if numero + numero > numero:
        su_signo = 1
    elif numero + numero < numero:
        su_signo = -1
    else:
        su_signo = 0
    return su_signo

def suma_lenta(numero, otro_numero):
    """
    Esta función hace una suma de 1 en 1,
    por ejemplo 4 + 3 aca seria 4 + 1 + 1 + 1.
    Pre: numero y otro_numero son números enteros,
    positivos o negativos.
    Post: la función devolvera la suma de los dos números.
    """
    sgn = signo(otro_numero)
    suma = numero
    if sgn == 1:
        for n in range(otro_numero):
            suma += 1
    elif sgn == -1:
        for n in range(abs(otro_numero)):
            suma -= 1
    return suma

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida).
    """
    numero = int(input('Ingrese un número: '))
    otro_numero = int(input('Ingrese el número que le quiera sumar: '))
    resultado = suma_lenta(numero, otro_numero)
    print(resultado)

if __name__ == "__main__":
    principal()
