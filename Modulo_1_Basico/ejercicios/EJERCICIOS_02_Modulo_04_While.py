# EJERCICIOS - 02 - Modulo - 04 - While

import os
import math
import random # Para generar númreos aleatorios

linea = "===================================="
os.system('clear')
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

'''
print(f"---Ejercicio nº 4: Suma de números positivos")

num4e1 = int(input("Escribe un número: "))
resultado = 0

while (num4e1 > 0):
    resultado += num4e1
    num4e1 = int(input("Escribe un número: "))


print(f"Los números positivos introducidos suman {resultado}. Programa terminado")
'''


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

'''
print(f"---Ejercicio nº 5: Sumatorio comparado con el número inicial")


num5e1 = float(input("Escribe la cantidad límite: "))
sumatorio = 0 # Esta variable recogerá la suma total

while (num5e1 <=0): # Primer bucle: controla que el número introducido es mayor que 0 
    num5e1 = float(input("El número debe ser mayor que 0. Inténtalo de nuevo: ")) #y, en caso contrario vuelve a pedir un número

while (sumatorio < num5e1): # Segundo bucle: se repite hasta que la suma de los números introducidos superen el primer número
    num5e2 = float(input("Escribe un número: "))
    sumatorio += num5e2

print(f"Has superado el límite. La suma de los números introducidos es {sumatorio}.{fin}")
'''


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
No has escrito ningún número entre 8 y 20.
Programa terminado

Escribe un número: -10
Escribe un número mayor que -10: -5
Escribe un número entre -10 y -5: -8
Escribe un número entre -10 y -5: 100
Ha escrito 1 número entre -10 y -5.
Programa terminado
'''

'''
print(f"---Ejercicio nº 6: Máximo, mínimo e intervalo")

num6e1 = int(input("Escribe un número: "))
num6e2 = int(input(f"Escribe un número mayor que {num6e1}: "))
contador = 0

while (num6e2 < num6e1): # Primer bucle para manejar que se introduce un segundo número mayor al primero
    num6e2 = int(input(f"{num6e2} no es mayor que {num6e1}. Inténtalo de nuevo: "))

num6e3 = int(input(f"Escribe un número entre {num6e1} y {num6e2}: "))

while ((num6e3 >= num6e1) and (num6e3 <= num6e2)):
    contador += 1
    num6e3 = int(input(f"Escribe un número entre {num6e1} y {num6e2}: "))

if (contador == 0):
    print (f"No has escrito ningún número entre {num6e1} y {num6e2}.")
else:
    print(f"Ha escrito {contador} número entre {num6e1} y {num6e2}.")

print("Programa terminado")
'''

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


'''
print(f"---Ejercicio nº 7: Múltiplos de 5")

# Variables
num7e1 = int(input("Escribe un número múltiplo de 5: ")) # Pide el prime número múltiplo de 5
num7e2 = 0 # El número que se pide sucesivamente
contador = 0 # Cuenta el número de múltiplos de 5 introducidos
salir = False # Variable de control para pedir un nuevo múltiplo de 5

while (num7e1%5 != 0):
    num7e1 = int(input(f"{num7e1} no es un número múltiplo de 5. Inténtalo de nuevo: "))

contador += 1

while (salir !=True):
    otro = input("¿Quieres escribir otro número múltiplo de 5? (S/N) ").lower()
    if (otro == "s"):
        num7e1 = int(input("Escribe otro número múltiplo de 5: "))
        contador += 1
    else: 
        salir = True

print(f"Has escrito {contador} número múltiplo de 5.\nPrograma terminado")
'''


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



print(f"---Ejercicio nº 8: Descomponsición en factores primos")

num8e1 = int(input("Escribe un número mayor que 1: "))

while(num8e1 <= 1): # Primer bucle que comprueba que el número introducido es mayor que 1, si no pideo otro
    num8e1 = int(input(f"{num8e1} no es un número mayor que 1. Inténtalo de nuevo: "))

# Si el número introducido es mayor que 1 continúa el programa
# Variables listas
numeros_primos = []
factores_primos = []
resto_cero = 0

# Primero hay que rellenar la lista de números primos menores que el número introducido
variable_control = 2 # valor 2 para saltar el 1
while (variable_control <= num8e1): # mientras sea menor o igual que el número introducido
    resto_cero = 0 # Esta variable se actualiza para cada vuelta para comprobar en el siguient bucle los restos = 0
    for i in range(1,variable_control): # En este condicional se calcula el número de veces que el resto es 0
        if (variable_control%i==0):
            resto_cero += 1
    if (resto_cero < 2): # En este condicional se añade a la lista el número primo (antes ha tenido menos de dos veces un resto 0)
        numeros_primos.append(variable_control)
    variable_control +=1 # Se incrementa la variable de control para acercarse al num8e1 y salir del bucle
print(f"Números primos: {numeros_primos}") # Muestra los números primos

# Segundo: las divisiones para obtener los valores primos

variable_control = 2 # Vuelvo a utilizar la misma variable




print(f"{fin}")



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


print(f"---Ejercicio nº 9: Número aleatorio")
'''
# import random está arriba del todo
num9e1 = random.randint(1,6) # Entero entre 1 y 6 incluidos
otro_numero_9e = "s"
while (otro_numero_9e == "s"):
    num9e1 = random.randint(1,6) # Entero entre 1 y 6 incluidos
    print(f"{num9e1}")
    otro_numero_9e = input("Para generar un nuevo número pulsa S o s, otra tecla para terminar: ").lower()

print("Programa terminado.")
'''


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

'''
print(f"---Ejercicio nº 10: Lanzando un dado")


otro_numero_10e = "s" # Variable para mantenerse en el juego
puntuacion10e = 0 # Variable que acumula la puntuación. 

while (otro_numero_10e == "s"):
    num10e1 = random.randint(1,6) # Aquí se generan las tiradas aleatorias de los dados
    puntuacion10e += num10e1 # Se acumula la tirada a la puntuación de la partida
    print(f"Tirada actual: {num10e1} Total acumulado: {puntuacion10e}")
    otro_numero_10e = input("Para generar un nuevo número pulsa S o s, otra tecla para terminar: ").lower() # s/n para seguir o salir

print(f"Puntuación final: {puntuacion10e} - Programa terminado")
'''

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
Primer jugador: Tirada actual: 5 Total acumulado: 5
Segundo jugador: Tirada actual: 5 Total acumulado: 5
Para generar un nuevo número pulsa S o s, otra tecla para terminar: s
Primer jugador: Tirada actual: 4 Total acumulado: 9
Segundo jugador: Tirada actual: 5 Total acumulado: 10
Para generar un nuevo número pulsa S o s, otra tecla para terminar: n
****************************************************************
Vencedor: Segundo jugador. Resultado final: Jugador1: 9 - Jugador2: 10
'''

'''
print(f"---Ejercicio nº 11: Dados: dos jugadores")
otro_numero_11e = "s" # Variable para mantenerse en el juego

# Variables de los dados inicializadas a 0
dado_11e_Jugador1 = 0
dado_11e_Jugador2 = 0
puntuacion_11e_Jugador1 = 0 # Variable que acumula la puntuación del jugador 1
puntuacion_11e_Jugador2 = 0 # Variable que acumula la puntuación del jugador 1

# Variables de los strings
nueva_tirada = "Para generar un nuevo número pulsa S o s, otra tecla para terminar: "
vencedor11e = ["Primer jugador", "Segundo jugador"]
linea11e = "****************************************************************" 

# Bucle principal del juego
while (otro_numero_11e == "s"):
    # Lanzamiento de los dados
    dado_11e_Jugador1 = random.randint(1,6)
    dado_11e_Jugador2 = random.randint(1,6)
    # Acumulación de las tiradas a la puntuación
    puntuacion_11e_Jugador1 += dado_11e_Jugador1
    puntuacion_11e_Jugador2 += dado_11e_Jugador2
    # Imprime por pantalla el resultado de las tiradas en dos líneas
    print(f"Primer jugador: Tirada actual: {dado_11e_Jugador1} Total acumulado: {puntuacion_11e_Jugador1}")
    print(f"Segundo jugador: Tirada actual: {dado_11e_Jugador2} Total acumulado: {puntuacion_11e_Jugador2}")
    # Pregunta por otra tirada
    otro_numero_11e = input(f"{nueva_tirada}").lower()

# El resultado: una vez se sale del bucle
print(f"{linea}")
# Evaluación del empate o un vencedor
if (puntuacion_11e_Jugador1 == puntuacion_11e_Jugador2):
    print(f"Primer jugador y segundo jugador han empatado a {puntuacion_11e_Jugador1} puntos")
elif (puntuacion_11e_Jugador1 > puntuacion_11e_Jugador2):
    print(f"Vencedor: {vencedor11e[0]}. Resultado final: Jugador1: {puntuacion_11e_Jugador1} - Jugador2: {puntuacion_11e_Jugador2}")
else: 
    print(f"Vencedor: {vencedor11e[1]}. Resultado final: Jugador1: {puntuacion_11e_Jugador1} - Jugador2: {puntuacion_11e_Jugador2}")
'''


#12. Enunciado: Escribe un programa que simule un juego en el que dos jugadores lanzan su propio dado.
#Tras cada tirada se mostrará el valor obtenido en el lanzamiento y el total obtenido hasta
#ese instante por cada jugador. Tras cada tirada se preguntará a cada uno de los jugadoressi
#quieren volver a lanzar el dado o si desean terminar su partida.
#A partir del instante en que un jugador haya decidido no jugar el programa no debe volvera
#preguntarle.
'''
LANZANDO DOS DADOS II
Primer jugador: Tirada actual: 4 Total acumulado: 4
Segundo jugador: Tirada actual: 4 Total acumulado: 4
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

'''
print(f"---Ejercicio nº 12: Dos jugadores tiradas independientes")

otro_numero_12e = "s" # Variable para mantenerse en el juego

# Variables de los dados inicializadas a 0
dado_12e_Jugador1 = 0
dado_12e_Jugador2 = 0
puntuacion_12e_Jugador1 = 0 # Variable que acumula la puntuación del jugador 1
puntuacion_12e_Jugador2 = 0 # Variable que acumula la puntuación del jugador 1
sigue_jugando_12e_Jugador1 = True
sigue_jugando_12e_Jugador2 = True

# Variables de los strings
nueva_tirada = "Para generar un nuevo número pulsa S o s, otra tecla para terminar: "
vencedor12e = ""
linea12e = "****************************************************************" 
otro_numero_12e = "s" # Variable para mantenerse en el juego
while (sigue_jugando_12e_Jugador1 == True) or (sigue_jugando_12e_Jugador2 == True): 
    # Bucle que se repite mientras no abandonan los dos jugadores

    # Bloque de preguntas a los jugadores
    # Jugador 1
    if (sigue_jugando_12e_Jugador1 == True):
        otro_numero_12e = input(f"Jugador 1: {nueva_tirada}").lower()
        if (otro_numero_12e != "s"):
            print("Sale el Jugador 1")
            sigue_jugando_12e_Jugador1 = False
        else:
            print("Nueva tirada del jugador 1")
            # Se genera la tirada de los dados del jugador 1: número aleatorio
            dado_12e_Jugador1 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 1
            puntuacion_12e_Jugador1 += dado_12e_Jugador1
            # Se muestra la puntuación del jugador 1
            print(f"Primer jugador: Tirada actual: {dado_12e_Jugador1} Total acumulado: {puntuacion_12e_Jugador1}")

    # Jugador 2
    if (sigue_jugando_12e_Jugador2 == True):
        otro_numero_12e = input(f"Jugador 2: {nueva_tirada}").lower()
        if (otro_numero_12e != "s"):
            print("Sale el jugador 2")
            sigue_jugando_12e_Jugador2 = False
        else:
            print("Nueva tirada del jugador 2")
            # Se genera la tirada de los dados del jugador 2: número aleatorio
            dado_12e_Jugador2 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 2
            puntuacion_12e_Jugador2 += dado_12e_Jugador2
            # Se muestra la puntuación del jugador 12
            print(f"Segundo jugador: Tirada actual: {dado_12e_Jugador2} Total acumulado: {puntuacion_12e_Jugador2}")

#Cuando salen se hace el recuento final
if (puntuacion_12e_Jugador1 > puntuacion_12e_Jugador2):
    vencedor12e = "Primer jugador"
else:
    vencedor12e = "Segundo jugador"
print(f"Vencedor: {vencedor12e}. Resultado final: Jugador1: {puntuacion_12e_Jugador1} – Jugador2: {puntuacion_12e_Jugador2}")
'''



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

print(f"---Ejercicio nº 13: Dos jugadores: menos de 21 puntos")

otro_numero_13e = "s" # Variable para mantenerse en el juego

# Variables de los dados inicializadas a 0
dado_13e_Jugador1 = 0
dado_13e_Jugador2 = 0
puntuacion_13e_Jugador1 = 0 # Variable que acumula la puntuación del jugador 1
puntuacion_13e_Jugador2 = 0 # Variable que acumula la puntuación del jugador 1
sigue_jugando_13e_Jugador1 = True
sigue_jugando_13e_Jugador2 = True

# Variables de los strings
nueva_tirada = "Para generar un nuevo número pulsa S o s, otra tecla para terminar: "
vencedor13e = ""
linea13e = "****************************************************************" 
otro_numero_13e = "s" # Variable para mantenerse en el juego





while (sigue_jugando_13e_Jugador1 == True) or (sigue_jugando_13e_Jugador2 == True): #and (puntuacion_13e_Jugador1 < 22 or puntuacion_13e_Jugador2 < 22): 
    # Bucle que se repite mientras no abandonan los dos jugadores

    # Bloque de preguntas a los jugadores
    # Jugador 1
    if (sigue_jugando_13e_Jugador1 == True):
        otro_numero_13e = input(f"Jugador 1: {nueva_tirada}").lower()
        if (otro_numero_13e != "s"):
            print("Sale el Jugador 1")
            sigue_jugando_13e_Jugador1 = False
        else:
            print("Nueva tirada del jugador 1")
            # Se genera la tirada de los dados del jugador 1: número aleatorio
            dado_13e_Jugador1 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 1
            puntuacion_13e_Jugador1 += dado_13e_Jugador1
            # Se muestra la puntuación del jugador 1
            print(f"Primer jugador: Tirada actual: {dado_13e_Jugador1} Total acumulado: {puntuacion_13e_Jugador1}")


    # Jugador 2
    if (sigue_jugando_13e_Jugador2 == True):
        otro_numero_13e = input(f"Jugador 2: {nueva_tirada}").lower()
        if (otro_numero_13e != "s"):
            print("Sale el jugador 2")
            sigue_jugando_13e_Jugador2 = False
        else:
            print("Nueva tirada del jugador 2")
            # Se genera la tirada de los dados del jugador 2: número aleatorio
            dado_13e_Jugador2 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 2
            puntuacion_13e_Jugador2 += dado_13e_Jugador2
            # Se muestra la puntuación del jugador 12
            print(f"Segundo jugador: Tirada actual: {dado_13e_Jugador2} Total acumulado: {puntuacion_13e_Jugador2}")

#Cuando salen se hace el recuento final en varios bloques condicionales

#Primera condición: si han superado los 21 puntos: pierden los dos
if (puntuacion_13e_Jugador1 > 21 and puntuacion_13e_Jugador2 > 21):
    print(f"Han perdido los dos: Resultado final: Jugador1: {puntuacion_13e_Jugador1} – Jugador2: {puntuacion_13e_Jugador2}")

#Segunda condición: empate
elif (puntuacion_13e_Jugador1 == puntuacion_13e_Jugador2) and (puntuacion_13e_Jugador1 <= 21):
        print(f"Empate: Resultado final: Jugador1: {puntuacion_13e_Jugador1} – Jugador2: {puntuacion_13e_Jugador2}")

#Tercera condición: el resto de supuestos
# IMPORTANE:
# UNA DISYUNTIVA EN UN SOLO BLOQUE ENTRE PARÉNTESIS: Gana el jugador uno
    #a) en la situación normal que tiene más puntos que el jugador 2
        # O
    #b) pase lo que pase, tenga los puntos que tenga, el jugador 2 supera los 21 puntos

# Y, ADEMÁS, se tiene que producir siempre la condición que el jugador 1 no supere los 21 puntos para ganar
else:
    if ((puntuacion_13e_Jugador1 > puntuacion_13e_Jugador2) or (puntuacion_13e_Jugador2 > 21)) and (puntuacion_13e_Jugador1 <=21):
        vencedor13e = "Primer jugador"
    # En el resto de los casos, gana el jugador 2
    else:
        vencedor13e = "Segundo jugador"

#Impresión del resultado final
print(f"Vencedor: {vencedor13e}. Resultado final: Jugador1: {puntuacion_13e_Jugador1} – Jugador2: {puntuacion_13e_Jugador2}")








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