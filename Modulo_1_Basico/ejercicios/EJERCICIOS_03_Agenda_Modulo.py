
#main
def validar_menu(num):
    try:
        if ((int(num) <= 6)):
            return int(num)
        else:
            return -1
    except ValueError:
        return -1

#bifurcacion operaciones
def ejecutar_operacion(num):
    
    return (f'Has elegido {type(num)} operacion {num}')

def formar_diccionario():
    tuplaA = ("Maria", "Luis", "Pepe")
    tuplaB = (4,5,6)
    diccionario = dict(zip(tuplaA,tuplaB))
    print(diccionario)
