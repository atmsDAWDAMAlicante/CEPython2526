#EJERCICIOS NTREGABLES UD 02 - Modulo 04 - While
#Ejercicio nº 14
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

#Enunciado: 

import os
import random

os.system('clear')


print(f"---Ejercicio nº 14: Juego de Dados entregable")

otro_numero = "s" # Variable para mantenerse en el juego

# Variables de los dados inicializadas a 0
dado_Jugador1 = 0
dado_Jugador2 = 0
puntuacion_Jugador1 = 0 # Variable que acumula la puntuación del jugador 1
puntuacion_Jugador2 = 0 # Variable que acumula la puntuación del jugador 1
sigue_jugando_Jugador1 = True
sigue_jugando_Jugador2 = True

# Variables de los strings
nueva_tirada = "Para generar un nuevo número pulsa S o s, otra tecla para terminar: "
vencedor = ""
linea = "****************************************************************" 
otro_numero = "s" # Variable para mantenerse en el juego


# Bucle que se repite mientras no abandonan los dos jugadores

# Estas condiciones del bucle while no funcionan bien:
#while (sigue_jugando_Jugador1 == True or sigue_jugando_Jugador2 == True) and (puntuacion_Jugador1 <=21 or puntuacion_Jugador2 <= 21): 
#while (sigue_jugando_Jugador1 == True) or (sigue_jugando_Jugador2 == True): #and (puntuacion_Jugador1 <=21 or puntuacion_Jugador2 <= 21):

# Esta de abajo casi lo hace bien:
# while (sigue_jugando_Jugador1 == True or sigue_jugando_Jugador2 == True) and (puntuacion_Jugador1 <=21 or puntuacion_Jugador2 <= 201): 

# Esta lo hace mejor, pero no del todo bien:
#while ((sigue_jugando_Jugador1 == True or sigue_jugando_Jugador2 == True) and (puntuacion_Jugador1 <=21 or puntuacion_Jugador2 <= 21)): 

# Solución: seguir con la idea original de los ejercicios anteriores y evaluar, inmediatamente después, el valor de la puntuación en un if
while (sigue_jugando_Jugador1 == True or sigue_jugando_Jugador2 == True):

    # If que evalúa si la puntuación supera 21 puntos
    # Puesto aquí, al principio, evita que el programa pregunte por una segunda ronda de tirada de dados
    if (puntuacion_Jugador1 >=21) or (puntuacion_Jugador2 >=21):
        break
        sigue_jugando_Jugador1 = False
        sigue_jugando_Jugador2 = False

    # Bloque de preguntas a los jugadores
    # Jugador 1
    if (sigue_jugando_Jugador1 == True):
        otro_numero = input(f"Jugador 1: {nueva_tirada}").lower()
        if (otro_numero != "s"):
            print("Sale el Jugador 1")
            sigue_jugando_Jugador1 = False
        else:
            print("Nueva tirada del jugador 1")
            # Se genera la tirada de los dados del jugador 1: número aleatorio
            dado_Jugador1 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 1
            puntuacion_Jugador1 += dado_Jugador1
            # Se muestra la puntuación del jugador 1
            print(f"Primer jugador: Tirada actual: {dado_Jugador1} Total acumulado: {puntuacion_Jugador1}")


    # Jugador 2
    if (sigue_jugando_Jugador2 == True):
        otro_numero = input(f"Jugador 2: {nueva_tirada}").lower()
        if (otro_numero != "s"):
            print("Sale el jugador 2")
            sigue_jugando_Jugador2 = False
        else:
            print("Nueva tirada del jugador 2")
            # Se genera la tirada de los dados del jugador 2: número aleatorio
            dado_Jugador2 = random.randint(1,6)
            # Se actualiza la puntuación del jugador 2
            puntuacion_Jugador2 += dado_Jugador2
            # Se muestra la puntuación del jugador 12
            print(f"Segundo jugador: Tirada actual: {dado_Jugador2} Total acumulado: {puntuacion_Jugador2}")


print(linea)
#Cuando salen se hace el recuento final en varios bloques condicionales

#Primera condición: si han superado los 21 puntos: pierden los dos
if (puntuacion_Jugador1 > 21 and puntuacion_Jugador2 > 21):
    print(f"Han perdido los dos: Resultado final: Jugador1: {puntuacion_Jugador1} – Jugador2: {puntuacion_Jugador2}")

#Segunda condición: empate
elif (puntuacion_Jugador1 == puntuacion_Jugador2) and (puntuacion_Jugador1 <= 21):
        print(f"Empate: Resultado final: Jugador1: {puntuacion_Jugador1} – Jugador2: {puntuacion_Jugador2}")

#Tercera condición: el resto de supuestos
# IMPORTANE:
# UNA DISYUNTIVA EN UN SOLO BLOQUE ENTRE PARÉNTESIS: Gana el jugador uno
    #a) en la situación normal que tiene más puntos que el jugador 2
        # O
    #b) pase lo que pase, tenga los puntos que tenga, el jugador 2 supera los 21 puntos

# Y, ADEMÁS, se tiene que producir siempre la condición que el jugador 1 no supere los 21 puntos para ganar
else:
    if ((puntuacion_Jugador1 > puntuacion_Jugador2) or (puntuacion_Jugador2 > 21)) and (puntuacion_Jugador1 <=21):
        vencedor = "Primer jugador"
    # En el resto de los casos, gana el jugador 2
    else:
        vencedor = "Segundo jugador"
    #Impresión del resultado final
    print(f"Vencedor: {vencedor}. Resultado final: Jugador1: {puntuacion_Jugador1} – Jugador2: {puntuacion_Jugador2}")