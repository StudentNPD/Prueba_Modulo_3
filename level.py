# valores iniciales - 
# n_pregunta = 0
# continuar = 'y'
# correcto = True
# p_level = 10
# op_sys = 'cls' if sys.platform == 'win32' else 'clear'

def choose_level(n_pregunta, p_level):
    """
    Determina el nivel de dificultad de una pregunta en función del número de preguntas y la cantidad de preguntas por nivel.

    Parámetros:
        n_pregunta (int): El número de la pregunta actual.
        p_level (int): El nivel actual del usuario.

    Retorna:
        str: El nivel de dificultad de la pregunta, que puede ser "Nivel Básico", "Nivel Intermedio" o "Nivel Avanzado".
    """
    if n_pregunta/p_level > 2:
        return "avanzadas"
    elif n_pregunta/p_level > 1:
        return "intermedias"
    elif n_pregunta/p_level > 0:
        return "basicas"
            
    # Construir lógica para escoger el nivel
    ##################################################
    pass
    ##################################################
    
    return 

# TEST
if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
    
