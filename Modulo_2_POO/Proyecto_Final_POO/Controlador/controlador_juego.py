# CONTROLADOR QUE GESTIONA EL JUEGO

# Modelo
from Modelo.administrador_juego import Administrador_juego, obtener_personajes_para_menu, PERSONAJES

# Vista
from Vista.vista_cli import Vista_CLI


class Controlador_juego:

    def __init__(self, vista):
        self.vista = vista

    def iniciar_juego(self):

        while True:

            opcion = self.vista.menu_iniciar_juego()

            if opcion == 1:
                self.nuevo_juego()

            elif opcion == 2:
                self.guardar_partida()

            elif opcion == 0:
                self.vista.imprimir_mensaje("Adiós")
                break

    def nuevo_juego(self):
        self.vista.imprimir_mensaje("Empezamos el juego: ELIJE TU JUGADOR: ")

        #PRIMERA PARTE: El menú para obtener el índice del personaje que será el jugador
        todos_los_personajes = obtener_personajes_para_menu()
        # Aquí se recoge el índice
        numero_jugador = self.vista.menu_elegir_jugador(todos_los_personajes)
        # Se saca al jugador del cesto de personajes
        resto_enemigos = PERSONAJES
        jugador = resto_enemigos.pop(numero_jugador-1)
        
        self.vista.imprimir_mensaje(f'EL JUGADOR ES: {jugador["nombre"]}')
        los_otros = "LOS ENEMIGOS SON: "
        for i in resto_enemigos:
            los_otros += f'- {i["nombre"]}\n'
        self.vista.imprimir_mensaje(los_otros)



    def guardar_partida(self):
        self.vista.imprimir_mensaje("Partida guardada")
    