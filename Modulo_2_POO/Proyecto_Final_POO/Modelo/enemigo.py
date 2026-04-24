from Modelo.personaje import Personaje


# Clase Enemigo

class Enemigo(Personaje):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    #self.contador_ataques = 0


  def decidir_accion(self,atacante): # Aquí viene lo bueno

    if (atacante.vida + 3 < atacante.vida_max) and (atacante.pociones > 0):
      return 3 # Tomate la poción

    elif (atacante.contador_ataques >= 3):
      return 2 # Tira el Ataque Cargado
    
    elif (atacante.vida + 3 > atacante.vida_max) and (atacante.pociones > 0) and (atacante.contador_ataques >=3):
      return 2 # Tira el Ataque Cargado
    
    else: # En los demás casos ¡ATACA!
      return 1
