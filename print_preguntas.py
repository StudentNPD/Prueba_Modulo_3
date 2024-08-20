import preguntas as p

def print_pregunta(enunciado, alternativas):
    """Imprime el enunciado de una pregunta y sus alternativas.

     Parámetros:
        enunciado (str): El texto del enunciado de la pregunta.
        alternativas (list): Una lista de tuplas, donde cada tupla contiene la alternativa (str) y un valor booleano (int) que indica si la alternativa es correcta o no.

    Retorna:
        None
    """
    print(enunciado)
    letras = ['A', 'B', 'C', 'D']
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt[0]}")
    
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
