#EJERCICIOS NTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 5
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

#Enunciado: 

import os
import random


os.system("cls")
def agregar_una_vez(lista, elemento): #El ejercicio 5
    #print(f"---Ejercicio nº 5: Agregar elemento no repetido")
    # Se recibe la lista y se forma la primera parte del fstring
    try:
        resultado = f"La lista actual es: {lista}\nValor que quieres añadir a la lista: {elemento}"
        # Se busca el duplicado
        # for i in lista: --> me puedo ahorrar el bucle con un in
        if (elemento in lista): # Si el elemento está en la lista
            raise Exception
        else:
            # No está en la lista
            lista.append(elemento) # Lo añade a la lista
            # Se actualiza el fstring
            resultado += f"\nLa lista actual es: {lista}"
        return resultado
    except Exception:
        resultado += f"\nError: Imposible añadir elementos duplicados => {elemento}\nLa lista actual es: {lista}"
        return resultado

print(agregar_una_vez([1, 'pie', -2], 10))
print(agregar_una_vez([1, 'pie', -2], 'pie'))

