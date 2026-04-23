# CONTROLADOR QUE GESTIONA EL JUEGO

# Modelo
from Modelo.gestor_personajes import PERSONAJES, Gestor_personajes
from Modelo.combate import Combate
from Modelo.accion import Accion, Ataque, Ataque_Cargado, Usar_Pocion,Kame_Hame
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

    def preparar_personajes(self):
        #PRIMERA PARTE: Menú
        self.vista.imprimir_mensaje("Empezamos el juego: ELIJE TU JUGADOR: ")
      
        personajes_partida = Gestor_personajes(PERSONAJES)
        
        todos_los_personajes = personajes_partida.obtener_personajes_para_menu_CLI()
        # Aquí se recoge el índice del jugador desde la vista
        numero_jugador = self.vista.menu_elegir_jugador(todos_los_personajes)

        #SEGUNDA PARTE: separar jugador, enemigo (activo) y resto
        # Se saca al jugador del cesto de personajes
        jugador = Jugador(**personajes_partida.obtener_jugador(numero_jugador-1))
        enemigo = Enemigo(**personajes_partida.obtener_enemigo())
        #resto_enemigos = personajes_partida.obtener_resto()
        resto_enemigos = [ #Para recuperar objetos y no diccionarios
            Enemigo(**datos)
            for datos in personajes_partida.obtener_resto()
        ]
        # Esto de abajo para borrar cuando vea que va
        print(type(resto_enemigos[1]))
        self.vista.imprimir_mensaje(f'Has escogido a: {jugador.nombre} vida {jugador.vida}')
        self.vista.imprimir_mensaje(f'Tu adversario es: {enemigo.nombre} vida {enemigo.vida}')

        # Retornamos los jugadores
        return jugador, enemigo, resto_enemigos

    def nuevo_juego(self):
        # Cogemos los jugadores
        jugador, enemigo, resto_enemigos = self.preparar_personajes()
        # IMPORTANTE ENVIO AL ADMINISTRADOR DEL JUEGO DE LOS OBJETOS JUGADOR Y ENEMIGOS
        combate = Combate(jugador,enemigo, resto_enemigos) 
        # EMPIEZA LA BATALLA
        self.bucle_combate(combate)


    def bucle_combate(self, combate):
        self.combate = combate
        turno = True # Empieza siempre el jugador
        accion = None
        contador = 0 # contador de las jugadas
        while True:
            contador += 1 # vamos contando las jugadas a título informativo
            if (turno == True): # LE TOCA AL JUGADOR
                # SE DEFINEN LOS ROLES
                atacante = self.combate.jugador
                defensor = self.combate.enemigo
                # MOSTRAR INFORMACIÓN
                self.vista.imprimir_mensaje(f"Jugada nº {contador}: {atacante.nombre} contra {defensor.nombre}")
                # SE PIDE UNA ACCIÓN
                acto = Menus.menu(Menus.menu_combate) 

                # Opciones del Menú
                if (acto == 1):
                    accion = Ataque()
                    accion.ejecutar(atacante, defensor)
                
                elif (acto == 2):
                    accion = Ataque_Cargado()
                    accion.ejecutar(atacante, defensor)

                elif (acto == 3):
                    accion = Usar_Pocion()
                    accion.ejecutar(atacante, defensor)

                elif (acto == 4):
                    print("Partida guardada")
                    print("Fin")
                    break

                elif (acto == 5):
                    accion = Kame_Hame()
                    accion.ejecutar(atacante, defensor)

                else: # SALIR DEL JUGADOR
                    print("Fin")
                    break

                # MOSTRAMOS EL STATUS TRAS LA ACCIÓN
                self.mostrar_status(atacante, defensor)
                # CAMBIAMOS EL TURNO
                #turno = self.combate.turno_enemigo(turno) 
                turno = not turno

            else: # Cambian las tornas
                atacante = self.combate.enemigo
                defensor = self.combate.jugador
                self.vista.imprimir_mensaje(f"Jugada nº {contador}- {atacante.nombre} ataca a {defensor.nombre}")

                atacante.decidir_accion() # Se lo piensa
                defensor.vida -= 1 # De momento el jugador pierde 1 de vida
                self.mostrar_status(atacante, defensor)
                #turno = self.combate.turno_enemigo(turno) # Cambia turno
                turno = not turno

            # Ver si está vivo
            

            if (combate.jugador.estar_vivo(combate.jugador.vida) == False):
                print(f"{combate.jugador.nombre} HA MUERTO")
                print("FIN DEL JUEGO")
                break

            elif not combate.enemigo.estar_vivo(combate.enemigo.vida):
                print(f"{combate.enemigo.nombre} ha sido derrotado")
                nuevo = combate.nuevo_enemigo()

                if not nuevo:
                    print("¡¡¡HAS DERROTADO A TODOS LOS ENEMIGOS!!!")
                    break

                combate.enemigo = nuevo

            '''
            elif (combate.enemigo.estar_vivo(combate.enemigo.vida) == False):
                print(f"{combate.enemigo.nombre} ha sido derrotado")
                combate.enemigo = combate.nuevo_enemigo()

            if not self.combate.nuevo_enemigo():
                print(f'{len(self.combate.resto_enemigos)} enemigos restantes')
                print("¡¡¡HAS DERROTADO A TODOS LOS ENEMIGOS!!!")
                break
            '''

    def mostrar_status(self, atacante, defensor):
            self.vista.imprimir_mensaje("---- STATUS:")
            self.vista.imprimir_mensaje(f"--{atacante.nombre} vida: {atacante.vida}")
            self.vista.imprimir_mensaje(f"--{defensor.nombre} vida: {defensor.vida}")