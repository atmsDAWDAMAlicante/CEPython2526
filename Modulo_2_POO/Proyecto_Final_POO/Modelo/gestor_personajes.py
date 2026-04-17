

# Este archivo contiene :
# La variable inicial de los personajes de la serie de TV Dragones y Mazmorras
# otra clase: Gestion_Personajes

# Variable inicial de los personajes: todos 10 de vida (inicial y total), 2 de ataque, 
# 2 pociones (devuelven 3 puntos de vida) y están vivos (bool)



PERSONAJES = [
    {"nombre": "Arquero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Barbaro", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Acróbata", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Mago",  "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Ladrona", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Caballero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True}
]

# Clase Gestor_Personajes
class Gestor_Personajes: # no hereda de personaje
  def __init__(self,lista_personajes):
    self.lista_personajes = lista_personajes

  def obtener_personaje(self, numero):
    try:
      int(numero)
    except ValueError:
      print(f'Introduce un número entero')
      return False
    else:
      jugador = self.lista_personajes.pop(numero)
      return jugador

  def listar_personajes(self):
    for elemento in self.lista_personajes:
      print(elemento["nombre"])