################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número
solicitado expresado en grados, minutos y segundos
a segundos. Y otra que haga el cambio en el sentido
contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto
son 60 segundos.
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta función convierte un número sexadecimal a decimal.
    Pre: horas, minutos y segundos son números enteros positivos.
    Post: la función multiplica esos números y los deja convertidos
    en segundos.
    """
    horas_min = 60 * horas
    horas_sec = 60 * horas_min
    minutos_sec = 60 * minutos
    numero = segundos + horas_sec + minutos_sec
    return numero

def decimal_a_sexadecimal(numero):
    """
    Esta función convierte un número decimal a sexadecimal.
    Pre: numero son los segundos de la función anterior.
    Post: la función devuelve los segundos en horas, minutos y segundos
    en una tupla.
    """
    sexadecimal = [ ]
    minutos = numero // 60
    numero_resto = numero % 60
    horas = minutos // 60
    minutos_resto = minutos % 60
    sexadecimal.append(horas)
    sexadecimal.append(minutos_resto)
    sexadecimal.append(numero_resto)
    return tuple(sexadecimal)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    horas = int(input('Ingrese los grados: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))
    numero = sexadecimal_a_decimal(horas, minutos, segundos)
    resultado = decimal_a_sexadecimal(numero)
    print (f'La conversión a segundos es igual a: {numero}.')
    print (f'La conversión a grados, minutos y segundos es: {resultado}.')

if __name__ == "__main__":
    principal()
