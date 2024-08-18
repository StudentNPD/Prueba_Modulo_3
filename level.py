# valores iniciales - 
# n_pregunta = 0
# continuar = 'y'
# correcto = True
# p_level = 10
# op_sys = 'cls' if sys.platform == 'win32' else 'clear'

def choose_level(n_pregunta, p_level):

    if n_pregunta/p_level > 2:
        return "Nivel Avanzado"
    elif n_pregunta/p_level > 1:
        return "Nivel Intermedio"
    elif n_pregunta/p_level > 0:
        return "Nivel Básico"
            
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
    
