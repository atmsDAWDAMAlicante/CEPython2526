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


#3. Enunciado: Un cliente nos plantea un problema: Necesita un programa que facture el uso de un
#teléfono. El usuario informará de:
#• La tarifa por segundo que se va a aplicar.
#• Número de comunicaciones realizadas.
#• Duración de cada comunicación expresada en horas, minutos y segundos.
#Como resultado deberemos informar la duración en segundos y coste de cada comunicación.
#Todas las funciones que crees almacénalas en la archivo funciones.py.
'''
¿Cuánto céntimos cuesta 1 segundo de comunicación?: 0.2
¿Cuántas llamadas hay que facturar?: 2
¿Cuántas horas?: 0
¿Cuántos minutos?: 1
¿Cuántos segundos?: 10
Duración: 70 segundos. Coste: 14.0 c€.
¿Cuántas horas?: 0
¿Cuántos minutos?: 2
¿Cuántos segundos?: 5
Duración: 125 segundos. Coste: 25.0 c€.
'''
print(f"---Ejercicio nº 3: Coste llamadas en céntimos")


print(linea)


#4. Enunciado: Vamos a mejorar el programa anterior:
#-El coste de cada llamada se mostrará con el formato xx€, yycen.
#-Al terminar el programa mostrará el tiempo total consumido en formato hh:mm:ss y
#el coste total.
'''
¿Cuánto céntimos cuesta 1 segundo de comunicación?: .2
¿Cuántas llamadas hay que facturar?: 2
¿Cuántas horas?: 0
¿Cuántos minutos?: 5
¿Cuántos segundos?: 23
Duración: 323 segundos. Coste: 64 c€.
¿Cuántas horas?: 0
¿Cuántos minutos?: 59
¿Cuántos segundos?: 1
Duración: 3541 segundos. Coste: 708 c€.
Duración total: 1h 4m 24s
Coste total: 7€,72cen
'''
print(f"---Ejercicio nº 4: Coste llamadas en euros y céntimos")


print(linea)


#5. Enunciado: Crea un módulo de funciones con el nombre area.py y guárdalo dentro de la carpeta de los
#ejercicios. Define en este módulo las funciones necesarias para calcular la superficie de
#cualquier cuadrado, rectángulo, trapecio, triángulo, círculo y romboide.
print(f"---Ejercicio nº 5: Areas de figuras geométricas (sencillo)")


print(linea)

#6. Enunciado: Crea un programa que permita calcular superficies de cualquier
#tipo de cuadrado, rectángulo, trapecio, triángulo, círculo y romboide. El programa mostrará
#un menú inicial con las distintas opciones, solicitará los valores necesarios, calculará el
#resultado utilizando la función necesaria definida en el ejercicio anterior y mostrará el
#resultado por pantalla.
'''
Selecciona una opción
a) Superficie de un cuadrado
b) Superficie de un rectángulo
c) Superficie de un trapecio
d) Superficie de un triángulo
e) Superficie de un círculo
f) Superficie de un romboide
Selección:7
Opción incorrecta. Vuelve a intentarlo?: e
¿Longitud del radio?: 6.23
Superficie: 121.93432330583002
'''
print(f"---Ejercicio nº 6: Áreas de figuras geométricas (ENTREGABLE)")


print(linea)
