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
    """Esta funcion indica si el numero ingresado
    es positivo, negativo o cero"""
    if numero + numero > 0:
        el_signo = 'Es positivo'
    elif numero + numero < 0:
        el_signo = 'Es negativo'
    else:
        el_signo = 'Es cero'
    return el_signo

def principal():
    """
    Esta función es la que se encarga de la parte
    'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = float(input('Ingrese un numero:'))
    print(signo(numero))

if __name__ == "__main__":
    principal()
