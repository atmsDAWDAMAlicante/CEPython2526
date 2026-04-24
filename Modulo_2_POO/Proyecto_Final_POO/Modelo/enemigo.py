from Modelo.personaje import Personaje


# Clase Enemigo

class Enemigo(Personaje):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    #self.contador_ataques = 0


  def decidir_accion(self,atacante): # Aquí viene lo bueno
    print(f'El {atacante.nombre} se está pensando qué hacer...')
    if (atacante.vida + 3 < atacante.vida_max) and (atacante.pociones > 0) and (atacante.contador_ataques < 3):
      return 3 # Tomate la poción

    elif (atacante.vida + 3 > atacante.vida_max) and (atacante.pociones > 0) and (atacante.contador_ataques >= 3):
      return 2 # Tira el Ataque Cargado
    
    #elif (atacante.pociones > 0) and (atacante.contador_ataques < 3):
      #return 3 # Tómate la poción que te quede
    
    else: # En los demás casos ¡ATACA!
      return 1
