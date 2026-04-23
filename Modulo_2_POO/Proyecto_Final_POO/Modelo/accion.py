# Módulo para gestionar las acciones: ataques y curarse con la poción

# clase padre Accion(combate)
class Accion: # sin constructor
  def ejecucion(self):
    return

class Ataque(Accion):
  def ejecutar(self, atacante, defensor):
    defensor.vida -= 1
    
class Ataque_Cargado(Accion):
  def ejecutar(self, atacante, defensor):
    defensor.vida -=5


class Usar_Pocion(Accion):
  def ejecutar(self, atacante, defensor):
    atacante.vida +=3
    
class Kame_Hame(Accion):
  def ejecutar(self, atacante, defensor):
    defensor.vida = 0

