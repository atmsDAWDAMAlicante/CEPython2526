# Crea la estructura de clases para el software de una cafetería, con los atributos y métodos
# indicados (sin implementar), basado en el siguiente diagrama de clases

from abc import ABC, abstractmethod # ESTO ES PORQUE EN EL DIAGRAMA DE CLASES HAY UNA CLASE ABSTRACTA LLAMADA INTERFAZ


class Producto: # CLASE PADRE de BEBIDA Y COMIDA
    def __init__(self, precio):
        self.__precio = precio
    
    # GETTERS Y SETTERS
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio

    def informacion(self):
        pass


class Bebida(Producto):
    def __init__(self, tamanyo, temperatura, precio):
        super().__init__(precio)
        self.__tamanyo = tamanyo
        self.__temperatura = temperatura

    # GETTERS Y SETTERS
    def get_tamanyo(self):
        return self.__tamanyo
    def set_tamanyo(self, tamanyo):
        self.__tamanyo = tamanyo
    def get_temperatura(self):
        return self.__temperatura
    
    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura
    
    def informacion(self):
        super().informacion()
        print(f"Tamanyo: {self.__tamanyo}, Temperatura: {self.__temperatura}")




def main():
    pass
if __name__ == "__main__":
    main()