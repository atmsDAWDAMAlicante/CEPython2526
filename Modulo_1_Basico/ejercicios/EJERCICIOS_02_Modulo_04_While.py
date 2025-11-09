# EJERCICIOS - 02 - Modulo - 04 - While

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")

fin = "\nPrograma finalizado"
#1. Enunciado: Escribe un programa que pida dos números enteros. El segundo número ha de ser mayor
#que el primero. En caso de no serlo, el programa volverá a solicitar el segundo número
#hasta que se cumpla la condición. Para terminar el programa debe mostrar los dos números
#por pantalla.

'''
Escribe un número entero: 6
Escribe un número entero mayor que 6: 6
6 no es mayor que 6. Vuelve a intentarlo: 1
1 no es mayor que 6. Vuelve a intentarlo: 8
Los números que has introducido son el 6 y el 8.
Programa finalizado
'''
'''
print(f"---Ejercicio nº 1: Dos enteros desiguales")
num1 = int(input("Escribe un número entero: "))

seguir = True # Variable de control

while (seguir != False):
    num2 = int(input(f"Escribe un número entero mayor que {num1}: ")) # Se repite el input hasta que se cumpla la condición
    if (num1 >= num2):
        print(f"{num2} no es mayor que {num1}. Vuelve a intentarlo")
        seguir = True
    else:
        seguir = False #Cambio en la variable de control

print(f"Los números que has introducido son el {num1} y el {num2}.{fin}")

'''


#2. Enunciado: Escribe un programa que pida un primer número. A partir de entonces el programa
#continuará pidiendo números hasta que el número introducido sea menor que el número
#inicial. En ese momento terminará la ejecución del programa.
'''
Escribe un número: 4.5
Escribe un número mayor que 4.5: 5
Escribe otro número mayor que 4.5:4.5
Escribe otro número mayor que 4.5: 2
2.0 es menor que 4.5.
Programa finalizado
'''

'''
print(f"---Ejercicio nº 2: Número menor que el inicial")
num2e1 = float(input("Escribe un número: "))
seguir = True #Variable de control del bucle While

primera_vez = True
primera_vez_string = " un"

while (seguir != False):
    if (primera_vez == False): #Primer condicional maneja el string "uno"/"otro"
        primera_vez_string = " otro"
    #Ahora se introduce el número 2º

    num2e2 = float(input(f"Escribe{primera_vez_string} número mayor que {num2e1}: "))
    if (num2e2 < num2e1): #Si se introduce un segundo número menor que el primero, se debe interrumpir el bucle
        seguir = False #Aquí cambia la variable de control para salir del bucle
    #Seguimos dentro del bucle
    primera_vez = False #Se actualiza la variable que controla el string primera_vez = "otro"/"un" número

print (f"{num2e2} es menor que {num2e1}.{fin}")

'''




#3. Enunciado: Escribe el código de un programa que pida un número entero positivo. A continuación, el
#programa debe de pedir por pantalla esa cantidad de números positivos. El programa debe
#continuar pidiendo números positivos hasta que se hayan introducido la cantidad de
#números indicada en la primera variable. Como resultado final se indicará cuantos de los
#números introducidos cumplen la condición de ser positivos.
'''
¿Cuántos números positivos vas a introducir?: 3
Escribe el primer número: 10
Escribe otro número: 2
Escribe otro número: -5
Escribe otro número: 2
Has escrito 3 números positivos. Programa finalizado.

¿Cuántos números positivos vas a introducir?: 0
La cantidad debe ser mayor que 0. Inténtalo de nuevo: 1
Escribe el primer número: 1
Has escrito 1 número positivo. Programa finalizado.
'''

'''
print(f"---Ejercicio nº 3: Contador de números positivos introducidos")

num3e1 = int(input("¿Cuántos números positivos vas a introducir?: "))

while (num3e1 <=0): #primer bucle: controla que el primer número es superior a 0
    num3e1 = int(input("La cantidad debe ser mayor que 0. Inténtalo de nuevo: "))

# Se ha salido del bucle porque se ha introducido un número mayor que 0

# Variables necesarias
contador = 0 # contará las vueltas que se dan hasta alcanzar el número introducido
numeros_positivos = 0
primera_vez_string = " el primer"
primera_vez = True

# Se entra en el segundo bucle que pide los números

while (contador < num3e1+1):

    # Primero: ver si es la primera vuelta para controlar el string "uno"/"otro"
    if (primera_vez == False):
        primera_vez_string = " otro"

    # Segundo: se recoge el primer número
    num3e2 = int(input(f"Escribe{primera_vez_string} número: "))

    if (num3e2 > 0): # Condicional que contiene el contador de números positivos introducidos
        numeros_positivos += 1

    #Tercero: actualización de variables:
    #Actualización de la variable que controla las vueltas
    if (num3e1 == 1): # Si el número introducido es 1, el bucle sólo dará una vuelta
        contador = num3e1+1
    else: # en caso contrario dará tantas vueltas como sea el número 1 introducido
        contador += 1 

    primera_vez = False #Se actualiza la variable que controla el string "un"/"otro"


print(f"Has escrito {numeros_positivos} número positivo.{fin}")
'''

#4. Enunciado: Escribe un programa que pida números positivos. El programa debe finalizar cuando el
#usuario introduzca un número negativo, en ese momento se debe mostrar la suma de todos
#los números positivos que se hayan introducido.
'''
Escribe un número: 11
Escribe otro número: 3
Escribe otro número: 7
Escribe otro número: -1

Los números positivos introducidos suman 21.
Programa terminado

Escribe un número: -9
Los números positivos introducidos suman 0.
Programa terminado
'''

print(f"---Ejercicio nº 4: Suma de números positivos")

num4e1 = int(input("Escribe un número: "))
resultado = 0

while (num4e1 > 0):
    resultado += num4e1
    num4e1 = int(input("Escribe un número: "))


print(f"Los números positivos introducidos suman {resultado}. Programa terminado")

#5. Enunciado: Escribe un programa que pida por pantalla un valor positivo. A continuación, el programa
#pedirá números hasta que la suma de todos los números introducidos supere el valor del
#número inicial, mostrando el resultado de la suma.

'''
Escribe la cantidad límite: 13
Escribe un número: 5.2
Escribe otro número: -1
Escribe otro número: 9
Has superado el límite. La suma de los números introducidos es 13.2.
Programa finalizado

Escribe la cantidad límite: -3
El número debe ser mayor que 0. Inténtalo de nuevo: 0
El número debe ser mayor que 0. Inténtalo de nuevo: 5.5
Escribe un número: 7.2
Has superado el límite. La suma de los números introducidos es 7.2.
Programa finalizado
'''

def ejercicio_05(num):
    print(f"---Ejercicio nº 5: Dxxx")






#6. Enunciado: Crea un programa que debe comenzar pidiendo dos números enteros (mínimo y máximo).
#A continuación, el programa debe ir pidiendo números enteros situados entre esos valores
#máximo y mínimo. El programa concluye cuando escribamos un número no comprendido
#entre los dos valores iniciales, mostrando la cantidad de números escritos incluidos en el
#intervalo abierto definido.

'''
Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Inténtalo de nuevo: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 6
Escribe otro número entre 6 y 50: 4
Ha escrito 2 números entre 6 y 50.
Programa terminado

Escribe un número: 8
Escribe un número mayor que 8: 20
Escribe un número entre 8 y 20: 45
No has escrito ningún número entre 6 y 50.
Programa terminado

Escribe un número: -10
Escribe un número mayor que -10: -5
Escribe un número entre -10 y -5: -8
Escribe un número entre -10 y -5: 100
Ha escrito 1 número entre -10 y -5.
Programa terminado
'''


def ejercicio_06(num):
    print(f"---Ejercicio nº 6: Dxxx")






#7. Enunciado: Escribe el código que pida números múltiplos de cinco mientras el usuario indique que
#quiere seguir introduciendo números. Para indicar que queremos introducir un nuevo
#número, el usuario deberá contestar S a una pregunta.

'''
Escribe un número múltiplo de 5: 10
¿Quieres escribir otro número múltiplo de 5? (S/N) S
Escribe otro número múltiplo de 5: 15
¿Quieres escribir otro número múltiplo de 5? (S/N) N
Has escrito 2 números múltiplos de 5.
Programa terminado

Escribe un número múltiplo de 5: 6
6 no es un número múltiplo de 5. Inténtalo de nuevo: 35
¿Quieres escribir otro número múltiplo de 5? (S/N) x
Has escrito 1 número múltiplo de 5.
Programa terminado
'''


def ejercicio_07(num):
    print(f"---Ejercicio nº 7: Dxxx")






#8. Enunciado: Realiza la descomposición en factores primos de un número dado por teclado.

'''
Escribe un número mayor que 1: 500
Descomposición en factores primos: 2 2 5 5 5
Escribe un número mayor que 1: 521
Descomposición en factores primos: 521
Escribe un número mayor que 1: 1
1 no es un número mayor que 1. Inténtalo de nuevo: 720
Descomposición en factores primos: 2 2 2 2 3 3 5
'''


def ejercicio_08(num):
    print(f"---Ejercicio nº 8: Dxxx")







#9. Enunciado: Escribe un programa que simule el funcionamiento de un dado, generando un número
#entero al azar entre 1 y 6. A continuación el programa preguntará si queremos generar un
#nuevo número aleatorio. Si contestamos ‘S’ o ‘s’ el programa volverá a ejecutarse y en
#cualquier otro caso finalizará.

'''
GENERADOR DE NÚMEROS ALEATORIOS
3
Para generar un nuevo número pulsa S o s, otra tecla para terminar: s
6
Para generar un nuevo número pulsa S o s, otra tecla para terminar: n
Programa terminado.
'''

def ejercicio_09(num):
    print(f"---Ejercicio nº 9: Dxxx")



#10. Enunciado: Modifica el programa anterior de tal forma que tras cada lanzamiento del dado elprograma
#también muestre la suma conseguida en todos los lanzamientos.

'''
LANZANDO UN DADO
Tirada actual: 4 Total acumulado: 4
Para generar un nuevo número pulsa S o s, otra tecla para terminar: s
Tirada actual: 2 Total acumulado: 6
Para generar un nuevo número pulsa S o s, otra tecla para terminar: S
Tirada actual: 4 Total acumulado: 10
Para generar un nuevo número pulsa S o s, otra tecla para terminar: n
Puntuación final: 10 - Programa terminado
'''


def ejercicio_10(num):
    print(f"---Ejercicio nº 10: Dxxx")


#11. Enunciado: Modifica el programa anterior para que ahora se muestren dos números al azar (dos
#jugadores) entre 1 y 6. Al terminar el juego el programa debe declarar ganador al jugador
#que haya obtenido más puntos.

'''
LANZANDO DOS DADOS
Primer jugador: Tirada actual: 2
Segundo jugador: Tirada actual: 5
Total acumulado: 2
Total acumulado: 5
Para generar un nuevo número pulsa S o s, otra tecla para terminar: s
Primer jugador: Tirada actual: 4 Total acumulado: 6
Segundo jugador: Tirada actual: 1 Total acumulado: 6
Para generar un nuevo número pulsa S o s, otra tecla para terminar: n
****************************************************************
Primer jugador y segundo jugador han empatado a 6 puntos
****************************************************************


LANZANDO DOS DADOS
Primer jugador: Tirada actual: 5
Segundo jugador: Tirada actual: 5
Total acumulado: 5
Total acumulado: 5
Para generar un nuevo número pulsa S o s, otra tecla para terminar: s
Primer jugador: Tirada actual: 4 Total acumulado: 9
Segundo jugador: Tirada actual: 5 Total acumulado: 10
Para generar un nuevo número pulsa S o s, otra tecla para terminar: n
****************************************************************
Vencedor: Segundo jugador. Resultado final: Jugador1: 9 - Jugador2: 10
'''


def ejercicio_11(num):
    print(f"---Ejercicio nº 11: Dxxx")



#12. Enunciado: Escribe un programa que simule un juego en el que dos jugadores lanzan su propio dado.
#Tras cada tirada se mostrará el valor obtenido en el lanzamiento y el total obtenido hasta
#ese instante por cada jugador. Tras cada tirada se preguntará a cada uno de los jugadoressi
#quieren volver a lanzar el dado o si desean terminar su partida.
#A partir del instante en que un jugador haya decidido no jugar el programa no debe volvera
#preguntarle.
'''
LANZANDO DOS DADOS II
Primer jugador: Tirada actual: 4
Segundo jugador: Tirada actual: 4
Total acumulado: 4
Total acumulado: 4
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Primer jugador: Tirada actual: 2 Total acumulado: 6
Segundo jugador: Tirada actual: 3 Total acumulado: 7
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: n
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Primer jugador: Tirada actual: 0 Total acumulado: 6
Segundo jugador: Tirada actual: 2 Total acumulado: 9
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: n
****************************************************************
Vencedor: Segundo jugador. Resultado final: Jugador1: 6 – Jugador2: 9
****************************************************************
'''
def ejercicio_12(num):
    print(f"---Ejercicio nº 12: Dxxx")





#13. Enunciado: Modifica el programa anterior para que el programa declare como ganador al jugador
#que haya obtenido más puntos sin superar los 21 puntos.
#Ten en cuenta que existen muchos casos distintos:
    #• Un jugador gana al obtener más puntos que el otro sin tener más de 21 puntos.
    #• Un jugador gana cuando ha obtenido menos puntos que el otro, pero el otro
    #ha obtenido más de 21 puntos.
    #• Los dos jugadores empatan obteniendo una misma puntuación menor de 21.
    #• Los dos jugadores pierden cuando han obtenido más de 21 puntos.
'''
LANZANDO DOS DADOS II
Primer jugador: Tirada actual: 5 Total acumulado: 5
Segundo jugador: Tirada actual: 3 Total acumulado: 3
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s

Primer jugador: Tirada actual: 4 Total acumulado: 9
Segundo jugador: Tirada actual: 6 Total acumulado: 9
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: n
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s

Primer jugador: Tirada actual: 0 Total acumulado: 9
Segundo jugador: Tirada actual: 1 Total acumulado: 10
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: n
****************************************************************
Vencedor: Segundo jugador. Resultado final: Jugador1: 9 - Jugador2: 10
****************************************************************
'''
def ejercicio_13(num):
    print(f"---Ejercicio nº 13: Dxxx")



#14. ENTREGABLE - Enunciado: Modifica el programa anterior de tal forma que cuando uno o los dos
#jugadores supere los 21 puntos, el juego de la partida por terminada y muestre el resultado final.

'''
Primer jugador: Tirada actual: 5 Total acumulado: 18
Segundo jugador: Tirada actual: 4 Total acumulado: 20
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s

Primer jugador: Tirada actual: 6 Total acumulado: 24
Segundo jugador: Tirada actual: 4 Total acumulado: 24
****************************************************************
Los dos jugadores han perdido por superar los 21 puntos
****************************************************************

Primer jugador: Tirada actual: 6 Total acumulado: 14
Segundo jugador: Tirada actual: 2 Total acumulado: 8
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: s

Primer jugador: Tirada actual: 4 Total acumulado: 18
Segundo jugador: Tirada actual: 2 Total acumulado: 10
Jugador 1: Para lanzar el dado pulsa S o s, otra tecla para terminar: s
Jugador 2: Para lanzar el dado pulsa S o s, otra tecla para terminar: n

Primer jugador: Tirada actual: 6 Total acumulado: 24
Segundo jugador: Tirada actual: 0 Total acumulado: 10
****************************************************************
Vencedor: Segundo jugador. El primer jugador sobrepasó los 21 puntos
****************************************************************
'''




def ejercicio_14(num):
    print(f"---Ejercicio nº 14: Dxxx")



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")