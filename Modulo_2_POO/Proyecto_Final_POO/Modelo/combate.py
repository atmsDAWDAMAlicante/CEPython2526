
# Modelo
from Modelo.jugador import Jugador
from Modelo.enemigo import Enemigo

# Los personajes de Dragones y Mazmorras

PERSONAJES = [
    {"nombre": "Arquero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Barbaro", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Acróbata", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Mago",  "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Ladrona", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Caballero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True}
]

def obtener_personajes_para_menu():
    texto_menu = ""
    # Usamos enumerate para obtener el índice y el diccionario del personaje
    for i, personaje in enumerate(PERSONAJES):
        # i + 1 para que el menú empiece con uno
        # Se forma el string pero con salto de línea para que se vea más bonito
        texto_menu += f"{i + 1} - {personaje['nombre']}\n"
        # Ahora se devuelve un diccionario que es lo que habrá que mandar a la Vista para el menú
    return {"texto":texto_menu,"lim":len(PERSONAJES)}


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