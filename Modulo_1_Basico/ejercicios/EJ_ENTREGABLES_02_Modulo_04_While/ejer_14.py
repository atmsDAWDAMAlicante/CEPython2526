#EJERCICIOS ENTREGABLES UD 02 - Modulo 04 - While
#Ejercicio nº 14
#ALUMNO: ANGEL TOMÁS MORENO SENÉN

#Enunciado: Modifica el programa anterior de tal forma que cuando uno o los dos
#jugadores supere los 21 puntos, el juego de la partida por terminada y muestre el resultado final.

import os
# para limpiar la terminal
os.system('cls')

import random # para generar los números aleatorios

# 1. Variables globales

otro_numero = "s" # Variable para mantenerse en el juego

# 1.1 Variables de los dados inicializadas a 0
dado_Jugador1 = 0
dado_Jugador2 = 0
puntuacion_Jugador1 = 0 # Variable que acumula la puntuación del jugador 1
puntuacion_Jugador2 = 0 # Variable que acumula la puntuación del jugador 1

# 1.2 Variables booleanas de los jugadores
sigue_jugando_Jugador1 = True
sigue_jugando_Jugador2 = True

# 1.3 Variables de los strings
nueva_tirada = "Para generar un nuevo número pulsa S o s, otra tecla para terminar: "
vencedor = ""
linea = "****************************************************************" 
otro_numero = "s" # Variable para mantenerse en el juego

# 2. La función que mantiene la partida con un bucle while

def partida_de_dados():
    # Problema inesperado con las variables globales dentro de la función
    # Solución, declarar las variables como globales
    # Esto sucede porque las variables se van a modificar dentro de la función
    global sigue_jugando_Jugador1
    global sigue_jugando_Jugador2
    global puntuacion_Jugador1
    global puntuacion_Jugador2

    # Bucle while que mantiene la partida mientras no salga los jugadores
    while (sigue_jugando_Jugador1 == True or sigue_jugando_Jugador2 == True):

        # A) If que evalúa si la puntuación supera 21 puntos
        # Puesto aquí, al principio, evita que el programa pregunte por una segunda 
        # ronda de tirada de dados
        if (puntuacion_Jugador1 >=21) or (puntuacion_Jugador2 >=21):
            break
            sigue_jugando_Jugador1 = False
            sigue_jugando_Jugador2 = False

        # B) Bloque de preguntas a los jugadores si siguen jugando
        # Jugador 1
        if (sigue_jugando_Jugador1 == True):
            otro_numero = input(f"Jugador 1: {nueva_tirada}").lower()
            if (otro_numero != "s"):
                print("Sale el Jugador 1") # Informa que abandona el juego
                sigue_jugando_Jugador1 = False # Se actualiza la variable para no preguntarle más
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
                print("Sale el jugador 2") # Informa que abandona el juego
                sigue_jugando_Jugador2 = False # Se actualiza la variable para no preguntarle más
            else:
                print("Nueva tirada del jugador 2")
                # Se genera la tirada de los dados del jugador 2: número aleatorio
                dado_Jugador2 = random.randint(1,6)
                # Se actualiza la puntuación del jugador 2
                puntuacion_Jugador2 += dado_Jugador2
                # Se muestra la puntuación del jugador 12
                print(f"Segundo jugador: Tirada actual: {dado_Jugador2} Total acumulado: {puntuacion_Jugador2}")
        # Finalizado el bucle se llama a una función para imprimir el resultado
        #recuento_final(puntuacion_Jugador1, puntuacion_Jugador2)
        recuento_final()

def recuento_final():
# Como las variables de la puntuación son globales no hace falta pasarlas
#def recuento_final(puntuacion_Jugador1, puntuacion_Jugador2):

    #A continuación se hace el recuento final en varios bloques condicionales

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


#Inicio del programa
print(f"---Ejercicio nº 14: Juego de Dados entregable")
partida_de_dados()