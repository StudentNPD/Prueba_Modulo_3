import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Mezcla el orden de las alternativas de una pregunta.

    Parámetros:
    pregunta (dict): Un diccionario que contiene la información de una pregunta, incluyendo sus alternativas.

    Retorna:
    list: Una lista con las alternativas de la pregunta en un orden aleatorio.
    """
    #mezclar alternativas
    #######################################################################
    random.shuffle(pregunta['alternativas'])
    #######################################################################
    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
