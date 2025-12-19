# EJERCICIOS - 03 - Modulo - 02 - 01 - Funciones II

# PRIMERA PARTE - CÁLCULOS DE SEGUNDOS

#from Modulo_1_Basico.ejercicios.EJERCICIOS_03_02_01_b_funciones import *
from EJERCICIOS_03_02_01_b_funciones import *
#import EJERCICIOS_03_02_01_b_funciones as modulo
import os

# EJECUCIÓN: desde el directorio raiz
# python -m ejercicios.EJERCICIOS_03_02_01_a_Segundos

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios del bloque Funciones 2\nPRIMERA PARTE - CÁLCULOS DE SEGUNDOS\n{linea}")


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
'''
Introduce el primer tiempo
horas: 5
minutos: 57
segundos: 3
Introduce el segundo tiempo
horas: 4
minutos: 4
segundos: 15
Introduce el tercer tiempo
horas: 0
minutos: 3
segundos: 59
Tiempo total: 10 h: 5 m: 17 s
'''
print(f"---Ejercicio nº 2: Suma total de tiempo")
tiempos = [[5,57,3],[4,4,15],[0,3,59]]

#for i in range (3):
#    tiempos.append(pedirNumeros(3))
print(tiempos)
#for j in range (len(tiempos)):
 #   print(f'{tiempos[j][1]}')
suma_tiempos(tiempos)

print(linea)





print(linea)
