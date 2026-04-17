
# Clase Enemigo

class Enemigo(Personaje):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

  def decidir_accion(self): # Aquí viene lo bueno
    print(f'El {self.nombre} se está pensando qué hacer...')
    return True