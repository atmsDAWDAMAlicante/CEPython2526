from Modelo.Trabajador import Trabajador

class Camarero(Trabajador):
    def __init__(self, nombre, dni, sueldo, lista_clientes):
        super().__init__(nombre, dni, sueldo)
        self.__lista_clientes = lista_clientes
    
    # GETTERS Y SETTERS
    def get_lista_clientes(self):
        return self.__lista_clientes
    def set_lista_clientes(self, lista_clientes):
        self.__lista_clientes = lista_clientes

    def tomar_pedido(self):
        pass

    def entregar_pedido(self):
        pass