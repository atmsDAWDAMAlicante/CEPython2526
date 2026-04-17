# Módulo para gestionar las acciones: ataques y curarse con la poción

# clase padre Accion(combate)
class Accion: # sin constructor
  def ejecucion(self):
    return

class Ataque(Accion):
  def ejecucion(self, activo):
    activo.vida -= 1
    return activo.vida

class Ataque_Cargado(Accion):
  def ejecucion(self, activo):
    activo.vida -=5
    return activo.vida

class Usar_Pocion(Accion):
  def ejecucion(self, activo):
    activo.vida +=3
    return activo.vida

