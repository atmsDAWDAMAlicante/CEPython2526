# CONTROLADOR QUE GESTIONA EL JUEGO

# Modelo
from Modelo.combate import PERSONAJES, obtener_personajes_para_menu, Combate

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

        # ELECCIÓN DEL JUGADOR
        self.vista.imprimir_mensaje("Empezamos el juego: ELIJE TU JUGADOR: ")

        #PRIMERA PARTE: El menú para obtener el índice del personaje que será el jugador
        todos_los_personajes = obtener_personajes_para_menu()
        # Aquí se recoge el índice
        numero_jugador = self.vista.menu_elegir_jugador(todos_los_personajes)
        # Se saca al jugador del cesto de personajes
        resto_enemigos = PERSONAJES
        jugador = resto_enemigos.pop(numero_jugador-1)
        enemigo = resto_enemigos.pop(0)
        
        
        self.vista.imprimir_mensaje(f'Has elegido al/a la: {jugador["nombre"]}\nAhora vas a luchar contra {enemigo["nombre"]}')
        los_otros = "y después te enfrentarás:\n"
        for i in resto_enemigos:
            los_otros += f'- {i["nombre"]}\n'
        self.vista.imprimir_mensaje(los_otros)

        # ENVIO AL ADMINISTRADOR DEL JUEGO DE LOS OBJETOS JUGADOR Y ENEMIGOS
        nueva_partida = Combate(jugador,enemigo, resto_enemigos) 
        print(nueva_partida.__dict__)


    def guardar_partida(self):
        self.vista.imprimir_mensaje("Partida guardada")
    