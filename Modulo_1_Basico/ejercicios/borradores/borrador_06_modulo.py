def suma(a,b):
    '''Esto sirve para sumar'''
    return a+b

class miExcepcion(Exception):
    pass

def dividir(a,b):
    try:
        if (b == 0):
            raise miExcepcion
        else:
            return a/b
    except miExcepcion:
        return "División por cero"