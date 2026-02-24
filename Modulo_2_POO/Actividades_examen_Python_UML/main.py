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

from Modelo.Validaciones import Validaciones
# Importar Vista
from Vista.Entradas import Introducciones
from Vista.Salidas import Menus, Resultados

from Controlador import Controlador




class Estatico:
    @staticmethod
    def saludar():
        print("Hola")
        


def main():
    os.system("cls")

    #while True:
     #   opcion_principal = M


    Menus.principal()
    Resultados.principal()
    Controlador.controleitor()
    plantilla = []
    cocacola = Bebida("Coca-Cola", "Grande", "Fria", 1.2)
    cocacola.informacion()
    pepe = Trabajador("Pepe", "12345678A", 1200)
    paco = Camarero("Paco", "87654321B", 1500, ["Cliente1", "Cliente2"])
    luis = Cocinero("Luis", "11223344C", 1300)
    print(pepe._id)
    print(paco._id) 
    print(luis._id)
    Estatico.saludar()
    plantilla.append(pepe)
    plantilla.append(paco)
    plantilla.append(luis)
    
    trab1 = Introducciones.crear_trabajador(2)
    print(trab1)
    dni_valido = Validaciones.validar_dni(trab1["dni"])
    print(dni_valido)
    while (dni_valido == False):
        trab1["dni"] = Introducciones.reiterar_entrada()
        dni_valido = Validaciones.validar_dni(trab1["dni"])
    #nuevo_trab = Cocinero(trab1["nombre"], trab1["dni"],trab1["sueldo"])
    #print(nuevo_trab.__dict__)
    plantilla.append(Trabajador(trab1["nombre"], trab1["dni"],trab1["sueldo"]))
    for i in plantilla:
        print(f'id: {i._id} - nombre: {i.nombre}')
        print(i.__dict__)
if __name__ == "__main__":
    main()