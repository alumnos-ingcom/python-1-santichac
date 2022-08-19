################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero
indicado es Primo.
"""

def es_primo(numero):
    """
    Esta función indica si un número es primo o no.
    Pre: numero es un número entero positivo.
    Post: la función devuelve True si el número es primo y
    False si el número no es primo.
    """
    devolucion = True
    for n in range(2, numero):
        if numero % n == 0:
            devolucion = False
    if numero == 1:
        devolucion = False
    
    return devolucion
    

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un numero: '))
    resultado = es_primo(numero)

    if resultado:
        print('El número es primo')
    else:
        print('El número no es primo')

if __name__ == "__main__":
    principal()
