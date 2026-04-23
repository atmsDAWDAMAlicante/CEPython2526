# CONTROLADOR QUE GESTIONA EL JUEGO

# Modelo
from Modelo.gestor_personajes import PERSONAJES, Gestor_personajes
from Modelo.combate import Combate
from Modelo.accion import Accion, Ataque, Ataque_Cargado, Usar_Pocion
from Modelo.jugador import Jugador
from Modelo.enemigo import Enemigo

# Vista
from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus, Vista_CLI

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
    def guardar_partida(self):
        self.vista.imprimir_mensaje("Partida guardada")
    

    def nuevo_juego(self):
        # ELECCIÓN DEL JUGADOR
        self.vista.imprimir_mensaje("Empezamos el juego: ELIJE TU JUGADOR: ")

        
        #PRIMERA PARTE: Obtención de los personajes:
        personajes_partida = Gestor_personajes(PERSONAJES)
        # Se obtiene el menú
        todos_los_personajes = personajes_partida.obtener_personajes_para_menu_CLI()
        # Aquí se recoge el índice del jugador desde la vista
        numero_jugador = self.vista.menu_elegir_jugador(todos_los_personajes)
        # Se saca al jugador del cesto de personajes
        jugador = Jugador(**personajes_partida.obtener_jugador(numero_jugador-1))
        enemigo = Enemigo(**personajes_partida.obtener_enemigo())
        #resto_enemigos = personajes_partida.obtener_resto()
        resto_enemigos = [ #Para recuperar objetos y no diccionarios
            Enemigo(**datos)
            for datos in personajes_partida.obtener_resto()
        ]
        print(type(resto_enemigos[1]))
        self.vista.imprimir_mensaje(f'Has escogido a: {jugador.nombre}')
        self.vista.imprimir_mensaje(f'Tu adversario es: {enemigo.nombre}')

        # ENVIO AL ADMINISTRADOR DEL JUEGO DE LOS OBJETOS JUGADOR Y ENEMIGOS
        combate = Combate(jugador,enemigo, resto_enemigos) 
        self.bucle_combate(combate)


    def bucle_combate(self, combate):
        self.combate = combate
        turno = True
        activo = None
        accion = None
        contador = 0
        while True:
            contador += 1
            print(f"nº {contador} - vuelta del bucle")
            if (turno == True): # EL JUGADOR
                acto = Menus.menu(Menus.menu_combate)
                activo = self.combate.enemigo
                if (acto == 1):
                    activo.vida = Ataque().ejecucion(activo)
                    accion = "ataque"
                elif (acto == 2):
                    activo.vida = Ataque_Cargado().ejecucion(activo)
                    accion = "ataque cargado"
                elif (acto == 3):
                    activo.vida = Usar_Pocion().ejecucion(activo)
                    accion = "poción"
                elif (acto == 4):
                    print("Partida guardada")
                    print("Fin")
                    break
                else: # SALIR DEL JUGADOR
                    print("Fin")
                    break
                self.combate.ejecutar_accion(accion) # Jugador acciona
                turno = self.combate.turno_enemigo(turno) # Cambia a enemigo

            else: # Turno del ejemigo
                activo = self.combate.jugador # Cambia activo
                self.combate.enemigo.decidir_accion() # Se lo piensa
                activo.vida -= 1
                turno = self.combate.turno_enemigo(turno)
            print(f'---La vida de {activo.nombre} es {activo.vida} - TURNO: {turno}')
            activo.estoyVivo = activo.estar_vivo(activo.vida)


            if (self.combate.jugador.estoyVivo == False):
                print(f"{self.combate.jugador.nombre} pierde")
                print("Fin")
                break
            elif (self.combate.enemigo.estoyVivo == False):
                print(f"{self.combate.jugador.nombre} ha ganado al {self.combate.enemigo.nombre}")
            
            if (len(self.combate.resto_enemigos)>0):
                self.combate.enemigo = None
                self.combate.enemigo = Enemigo(**self.combate.resto_enemigos.pop(0))
            else:
                print("Fin del juego")
                break

