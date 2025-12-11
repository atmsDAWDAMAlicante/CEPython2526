# EJERCICIOS - 03 - Modulo - 02 - Funciones II
from ejercicios.EJERCICIOS_03_Modulo_02_funciones import *
import os

# EJECUCIÓN: desde el directorio raiz
# python -m ejercicios.EJERCICIO_03_Modulo_02

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios del bloque Funciones 2\n{linea}")


#1. Enunciado: Crea un programa que solicite tres valores de tiempo con el formato h:m:s. Donde h son
# horas, m minutos y s segundos. A través de una función se debe convertir cada uno de estos
# valores a segundos. El programa mostrará como resultado la suma de los tres valores en
# formato de segundos.
'''
print(f"---Ejercicio nº 1: Convertir tiempo en segundos")
resultado = pedirNumeros(3)
print(f'TOTAL: {convertir_a_segundos(resultado)} segundos')
print(linea)
'''
#2. Enunciado: Modifica el programa anterior para conseguir que el resultado de la 
# suma de los tres tiempos se muestre en formato de h:m:s
print(f"---Ejercicio nº 2: Suma total de tiempo")
tiempos = [[5,57,3],[4,4,15],[0,3,59]]

#for i in range (3):
#    tiempos.append(pedirNumeros(3))
print(tiempos)
#for j in range (len(tiempos)):
 #   print(f'{tiempos[j][1]}')
suma_tiempos(tiempos)

print(linea)


#3. Enunciado: 
print(f"---Ejercicio nº 3: XX")


print(linea)


#4. Enunciado: 
print(f"---Ejercicio nº 4: XX")


print(linea)


#5. Enunciado: 
print(f"---Ejercicio nº 5: XX")


print(linea)

#6. Enunciado: 
print(f"---Ejercicio nº 6: XX")


print(linea)
