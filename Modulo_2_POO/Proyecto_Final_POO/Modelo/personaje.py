

# Aquí está la clase padre Personaje
# Se produce la herencia
# Esta es la clase padre de Jugador y Enemigo

# Este archivo también contiene :
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

# Clase padre Personaje
class Personaje:
  def __init__(self, nombre, vida, vida_max, ataque, pociones, estoyVivo):
    self.nombre = nombre
    self.vida = vida
    self.vida_max = vida_max
    self.ataque = ataque
    self.pociones = pociones
    self.estoyVivo = estoyVivo

  def recibir_daño():
    pass

  def curarse():
    pass

  def estar_vivo(self, vida): #Este método informa si el personaje sigue vivo o ha muerto
    if (self.vida <= 0):
      return False
    else:
      return True

# Probando el constructor
nuevo = Personaje("guerrero",1,2,3,4,True)
print(nuevo.__dict__)

