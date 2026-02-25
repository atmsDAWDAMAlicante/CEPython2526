from Modelo.Trabajador import Trabajador # Ruta absoluta

class Camarero(Trabajador):
    def __init__(self, nombre, dni, sueldo, lista_clientes=[]):
        super().__init__(nombre, dni, sueldo)
        self.lista_clientes = lista_clientes # En el constructor SE ASIGNA el valor
    
    # Métodos propios de la clase Camarero
    def tomar_pedido(self):
        pass

    def entregar_pedido(self):
        pass