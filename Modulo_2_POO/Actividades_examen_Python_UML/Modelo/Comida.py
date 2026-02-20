from Modelo.Producto import Producto

    
class Comida(Producto):
    def __init__(self, nombre, precio, tipo, ingredientes):
        super().__init__(nombre, precio)
        self.tipo = tipo
        self.ingredientes = ingredientes
   