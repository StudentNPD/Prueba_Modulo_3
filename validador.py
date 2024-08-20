def validate(opciones, eleccion):
    """Valida la elección del usuario y la devuelve si es válida.

     Parámetros::
        opciones (list): Una lista de las opciones válidas.
        eleccion (str): La elección del usuario.

    Retorna:
        str: La elección del usuario si es válida.
    """
    while eleccion not in opciones:
        print(f'Opción no válida, ingrese una de las opciones válidas: {opciones}')
        eleccion = input("Ingresa una opción: ")
    return eleccion

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
