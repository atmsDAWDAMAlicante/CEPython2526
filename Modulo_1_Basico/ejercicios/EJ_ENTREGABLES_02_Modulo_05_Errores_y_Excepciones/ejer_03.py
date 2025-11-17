#EJERCICIOS NTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 3
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

#Enunciado: 

import os
import random

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