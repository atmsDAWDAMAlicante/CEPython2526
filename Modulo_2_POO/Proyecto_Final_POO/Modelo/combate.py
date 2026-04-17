



class Combate:
    def __init__(self, jugador, enemigo, resto_enemigos):
        self.jugador = jugador
        self.enemigo = enemigo
        self.resto_enemigos = resto_enemigos

    def nuevo_enemigo(self):
        pass

    def ejecutar_accion(self, accion):
        print(f'El {self.jugador.nombre} hace {accion}')

    def turno_enemigo(self, turno):
        turno = not turno

        if (turno == True):
            print(f'Ahora le toca a {self.jugador.nombre}')

        else:
            print(f'Ahora le toca a {self.enemigo.nombre}')


        return turno

    def comprobar_enemigo():
        print(f'xx tiene x vida')