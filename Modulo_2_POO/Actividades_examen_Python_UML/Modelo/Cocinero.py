from .Trabajador import Trabajador # Ruta relativa

class Cocinero(Trabajador):
    def __init__(self, nombre, dni, sueldo):
        super().__init__(nombre, dni, sueldo) # En el diagrama de clases no tiene atributos propios

    # Métodos propios de la clase Cocinero
    def preparar_pedido():
        pass