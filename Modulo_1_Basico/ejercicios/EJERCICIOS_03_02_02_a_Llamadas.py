# EJERCICIOS - 03 - Modulo - 02 - 02 - Funciones II

# SEGUNDA PARTE - LLAMADAS TELEFÓNICAS

#from Modulo_1_Basico.ejercicios.EJERCICIOS_03_02_01_b_funciones import *
import os
import EJERCICIOS_03_02_02_b_funciones

# EJECUCIÓN: desde el directorio raiz
# python -m ejercicios.EJERCICIO_03_Modulo_02

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios del bloque Funciones 2\nSEGUNDA PARTE - LLAMADAS TELEFÓNICAS\n{linea}")




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



