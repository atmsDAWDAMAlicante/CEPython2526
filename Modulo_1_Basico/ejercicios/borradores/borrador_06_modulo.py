def suma(a,b):
    '''Esto sirve para sumar'''
    return a+b

class miExcepcion(Exception):
    pass

def dividir(a,b):
    try:
        if (b == 0):
            raise miExcepcion
        
    except miExcepcion:
        return "División por cero"
    else:
        return a/b
    finally:
        print("¿otra?")