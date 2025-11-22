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



def ejercicio_03(color):
    print(f"---Ejercicio nº 3: Diccionario de colores")
    colores = {'rojo':'red', 'verde':'green', 'azul':'blue', 'negro':'black'}
    try:
        colores.get(color) # esto no hace nada
        return f'{color} en inglés se dice {colores[color]}'
    except KeyError:
        return f'Error: El término {color} no se encuentra en este diccionario, debes probar con otro que sí exista.'
print(ejercicio_03("azul"))
print(ejercicio_03("amarillo"))