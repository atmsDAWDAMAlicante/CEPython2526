# Crea la estructura de clases para el software de una cafetería, con los atributos y métodos
# indicados (sin implementar), basado en el siguiente diagrama de clases

from abc import ABC, abstractmethod # ESTO ES PORQUE EN EL DIAGRAMA DE CLASES HAY UNA CLASE ABSTRACTA LLAMADA INTERFAZ
import os

# A) CLASE PADRE PRODUCTO Y CLASES HIJAS BEBIDA Y COMIDA

class Producto: # CLASE PADRE DE BEBIDA Y COMIDA
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def informacion(self):
        pass


class Bebida(Producto):
    def __init__(self, nombre, precio, tamanyo, temperatura):
        super().__init__(nombre, precio)
        self.tamanyo = tamanyo
        self.temperatura = temperatura
    
    #def informacion(self): # No es necesario sobreescribirlo
        #super().informacion()
    
class Comida(Producto):
    def __init__(self, nombre, precio, tipo, ingredientes):
        super().__init__(nombre, precio)
        self.tipo = tipo
        self.ingredientes = ingredientes
   


# B) CLASE CLIENTE

class Cliente:
    def __init__(self, nombre, lista_productos):
        self.nombre = nombre
        self.lista_productos = lista_productos

    def realizar_pedido(self):
        pass

# C) CLASE TRABAJADOR Y CLASES HIJAS CAMARERO Y COCINERO Y CLASE ABSTRACTA ESTADO (interfaz)

class Estado(ABC): # CLASE ABSTRACTA (INTERFAZ)
    @abstractmethod
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass


class Trabajador(Estado): # CLASE PADRE DE CAMARERO Y COCINERO 
    _id_autoincremental = 0 # ATRIBUTO DE CLASE CON UNA _ porque pone el diagrama que es PROTECTED (Java)
    # ESTE ATRIBUTO LO HEREDARÁN TODOS LOS TRABAJADORES, PERO SOLO SE USARÁ EN EL CONSTRUCTOR DE LA CLASE TRABAJADOR PARA ASIGNAR EL ID AUTOINCREMENTAL A CADA TRABAJADOR
    def __init__ (self, nombre, dni, sueldo):
        self.nombre = nombre
        self.__dni = dni
        self.__sueldo = sueldo
        Trabajador._id_autoincremental += 1
        self._id = Trabajador._id_autoincremental
        


    # GETTERS Y SETTERS
    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni

    def get_sueldo(self):
        return self.__sueldo
    def set_sueld(self, sueldo):
        self.__sueldo = sueldo



    
    # MÉTODOS DE LA CLASE ABSTRACTA ESTADO (INTERFAZ)
    def dar_de_alta(self):
        pass
    def dar_de_baja(self):
        pass



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

class Cocinero(Trabajador):
    def __init__(self, nombre, dni, sueldo):
        super().__init__(nombre, dni, sueldo)

    def preparar_pedido():
        pass








def main():
    os.system("cls")
    cocacola = Bebida("Coca-Cola", "Grande", "Fria", 1.2)
    cocacola.informacion()
    pepe = Trabajador("Pepe", "12345678A", 1200)
    paco = Camarero("Paco", "87654321B", 1500, ["Cliente1", "Cliente2"])
    luis = Cocinero("Luis", "11223344C", 1300)
    print(pepe._id)
    print(paco._id) 
    print(luis._id)

if __name__ == "__main__":
    main()