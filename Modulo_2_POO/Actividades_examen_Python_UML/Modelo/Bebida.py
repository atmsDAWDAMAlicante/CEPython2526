from Modelo.Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, tamanyo, temperatura):
        super().__init__(nombre, precio)
        self.tamanyo = tamanyo
        self.temperatura = temperatura
    
    #def informacion(self): # No es necesario sobreescribirlo
        #super().informacion()




