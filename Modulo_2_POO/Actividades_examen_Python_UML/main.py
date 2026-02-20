# Crea la estructura de clases para el software de una cafetería, con los atributos y métodos
# indicados (sin implementar), basado en el siguiente diagrama de clases

from abc import ABC, abstractmethod # ESTO ES PORQUE EN EL DIAGRAMA DE CLASES HAY UNA CLASE ABSTRACTA LLAMADA INTERFAZ
import os

from Modelo.Cliente import Cliente

from Modelo.Trabajador import Trabajador
from Modelo.Camarero import Camarero as Camarero
from Modelo.Cocinero import Cocinero as Cocinero 

from Modelo.Producto import Producto
from Modelo.Bebida import Bebida
from Modelo.Comida import Comida





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