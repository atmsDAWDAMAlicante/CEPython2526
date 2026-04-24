# Módulo para gestionar las acciones: ataques y curarse con la poción

# clase padre Accion(combate)
class Accion: # sin constructor
  def ejecucion(self):
    return

class Ataque(Accion):
  def ejecutar(self, atacante, defensor):
    defensor.vida -= 1
    atacante.contador_ataques += 1
    
class Ataque_Cargado(Accion):
  def ejecutar(self, atacante, defensor):
    if (atacante.contador_ataques > 2):
      defensor.vida -=5
      atacante.contador_ataques = 0
    else:
      print(f"Te falta {3-atacante.contador_ataques} Petit-Suis")
      defensor.vida -= 1
      atacante.contador_ataques += 1

class Usar_Pocion(Accion):
  def ejecutar(self, atacante, defensor):
    if (atacante.pociones > 0):
      atacante.pociones -= 1
      atacante.vida +=3
      if (atacante.vida > atacante.vida_max):
          atacante.vida = atacante.vida_max
      print(f"Te quedan {atacante.pociones} pociones")
    else:
      print(f"No te quedan pociones")
      
    
    
class Kame_Hame(Accion):
  def ejecutar(self, atacante, defensor):
    print("KAAAAAAME HAAAAAME HAAAAA!!!!!!!")
    defensor.vida = 0

