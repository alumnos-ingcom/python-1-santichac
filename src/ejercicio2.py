################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique
si el mismo es positivo, negativo o cero utilizando
sumas y restas.
"""
def signo(numero):
    """
    Esta funcion indica si el numero ingresado
    es positivo, negativo o cero.
    Pre: numero es un número entero o con coma, positivo o negativo
    Post: la función signo devolvera si el número ingresado es positivo devuelve 1,
    si es negativo devuelve -1 y si es cero devuelve 0.
    """
    if numero + numero > 0:
        el_signo = 1
    elif numero + numero < 0:
        el_signo = -1
    else:
        el_signo = 0
    return el_signo

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = float(input('Ingrese un numero:'))
    resultado = signo(numero)
    print(resultado)

if __name__ == "__main__":
    principal()
