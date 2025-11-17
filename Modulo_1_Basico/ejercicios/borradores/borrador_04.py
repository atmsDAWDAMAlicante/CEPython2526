# Funciones
import os
os.system("cls")
from random import randint
print(randint(2,4))

def prueba_ayuda(): 
    ''' Este es el mensaje de ayuda '''
    print("Mensaje de la función")
prueba_ayuda()

help(prueba_ayuda)

# Varios parámetros - tupla
def parametros_varios(*numeros):
    print(numeros)

parametros_varios(3,4,4,5,3)
parametros_varios("Hola", True)
parametros_varios("kjkljñ",3434,232)

def hora_apertura(dia="lunes",hora=9):
    print(f'El {dia}: se abre a las {hora}')

hora_apertura()
hora_apertura("Martes")
hora_apertura(2)
hora_apertura(hora=4)
hora_apertura("Jueves", 6)


def recoge_tupla(*args):
    for i in enumerate(args):
        print(f'{i}')

recoge_tupla(23,3,53,53,3,53,34,3,4,3,43,4,34,3,43,4)
