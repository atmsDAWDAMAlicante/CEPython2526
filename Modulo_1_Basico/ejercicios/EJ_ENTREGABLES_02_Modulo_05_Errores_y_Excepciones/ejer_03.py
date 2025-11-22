#EJERCICIOS ENTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 3
#ALUMNO: ANGEL TOMÁS MORENO SENÉN

#Enunciado: Partimos del siguiente diccionario:
    #colores = { 'rojo':'red', 'verde':'green', 'azul':'blue', 'negro':'black'}
# Crea un programa que solicite un término del diccionario para mostrar su valor asociado por
# pantalla:
    #Introduce el nombre de un color en español: azul
    #azul en inglés se dice blue
#En caso de que el término no esté incluido en el diccionario se producirá un error. Crea una
#excepción para evitar que el programa se bloquee y que explique al usuario la causa y
#solución.

import os
# para limpiar la terminal
os.system('cls')

#1. Variable global
colores = {'rojo':'red', 'verde':'green', 'azul':'blue', 'negro':'black'}

#2. Función que pide el color y valida si existe en la lista
def ejercicio_03():
    color = input("Introduce un color: ") # Pide un color
    try:
        #colores.get(color) # esto devolvería el valor y None si no estuviera en la lista
        print(f'{color} en inglés se dice {colores[color]}')
        #return f'{color} en inglés se dice {colores[color]}'
    except KeyError: # Si no está, lanza la excepción e imprime el resultado en la terminal
        print (f'Error: El término {color} no se encuentra en este diccionario, debes probar con otro que sí exista.')
        #return f'Error: El término {color} no se encuentra en este diccionario, debes probar con otro que sí exista.'


#Inicio del programa
print(f"---Ejercicio nº 3: Diccionario de colores")
ejercicio_03()

#ejercicio_03("azul")
#ejercicio_03("amarillo")