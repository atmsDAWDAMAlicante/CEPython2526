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
from Vista.Entradas import Introducciones, Menus_Entradas
from Vista.Salidas import Menus, Resultados

from Controlador import Controlador

menu_principal = [
    "1 - Crear trabajador",
    "2 - Crear producto",
    "3 - Asignar cliente a camarero",
    "4 - Modificar antigüedad",
    "5 - Realizar pedido",
    "6 - Tomar pedido",
    "7 - Entregar pedido",
    "8 - Preparar pedido",
    "9 - Inventario con __dict__",
    "0 - Salir"
]



class Estatico:
    @staticmethod
    def saludar():
        print("Hola")
        


def main():
    os.system("cls")

    while True:
        opcion_principal = Validaciones.validar_menu_principal(Menus_Entradas.mostrar_menu_principal(menu_principal))
        if opcion_principal == 0:
            print("="*5," Fin del programa")
            break
        elif (opcion_principal == -1):
            print(f'MAL {opcion_principal}')
        else:
            Controlador.flujo_menu_principal(opcion_principal)
        
    # Camareros iniciales
    camareros = []


    #camareros.append(Camarero("Paco", "87654321B", 1500, ["Cliente1", "Cliente2"]))
    camareros.append(Camarero("Pepe Pérez Pérez", "1111111A", 1205.32, []))
    camareros.append(Camarero("Manolo Martínez Martínez", "22222222B", 1132.45, []))
    camareros.append(Cocinero("Luisa López López", "11223344C", 1300.45))
    #luis = Cocinero("Luis", "11223344C", 1300)
    for i in camareros:
        if isinstance(i,Camarero):
            print(f'Camarero: {i.nombre}')
        else:
            print(f'{type(i).__name__}: {i.nombre}')

    Menus.principal()
    Resultados.principal()

    plantilla = []
    cocacola = Bebida("Coca-Cola", "Grande", "Fria", 1.2)
    cocacola.informacion()


    Estatico.saludar()

    #plantilla.append(luis)
    '''
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
    '''
    for i in plantilla:
        print(f'id: {i._id} - nombre: {i.nombre}')
        print(i.__dict__)

if __name__ == "__main__":
    main()