



class Combate:
    def __init__(self, jugador, enemigo, resto_enemigos):
        self.jugador = jugador
        self.enemigo = enemigo
        self.resto_enemigos = resto_enemigos

    def nuevo_enemigo(self):
        if len(self.resto_enemigos) > 0:
            return  self.resto_enemigos.pop(0)
            #return True
        #return False

'''
    def turno_enemigo(self, turno):
        turno = not turno

        if (turno == True):
            print(f'Ahora le toca a {self.jugador.nombre}')

        else:
            print(f'Ahora le toca a {self.enemigo.nombre}')


        return turno
'''