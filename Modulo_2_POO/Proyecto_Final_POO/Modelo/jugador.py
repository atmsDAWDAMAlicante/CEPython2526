from Modelo.personaje import Personaje

# Clase Jugador
# En el constructor se le suben los puntos de vida a 100, ataque a 10 y 5 pociones

# Clase jugador
class Jugador(Personaje):

  def __init__(self,**kwargs):
    #super().__init__(nombre, vida, vida_max, ataque, defensa, pociones)
    super().__init__(**kwargs) # Recoge los valores de la clase padre
    self.vida = 100
    self.vida_max = 100
    self.ataque = 10
    self.pociones = 5

  def ataque_cargado(self):
    print(f"{self.nombre} dispone de ataque cargado")