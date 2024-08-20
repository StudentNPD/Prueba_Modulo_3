import preguntas as p


def verificar(alternativas, eleccion):
    """Determina si la elección del usuario es correcta.

    Args:
        alternativas (list): Una lista de tuplas, donde cada tupla contiene la alternativa (str) y un valor booleano (int) que indica si la alternativa es correcta o no.
        eleccion (str): La elección del usuario, que debe ser 'a', 'b', 'c' o 'd'.

    Returns:
        bool: True si la elección del usuario es correcta, False de lo contrario.
    """
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)
    if alternativas[eleccion][1] == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    
    
    
    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






