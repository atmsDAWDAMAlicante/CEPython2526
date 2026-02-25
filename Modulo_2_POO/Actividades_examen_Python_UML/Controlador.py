
from Vista.Salidas import Menus_Salidas, Resultados
from Vista.Entradas import Introducciones
from Modelo.Validaciones import Validaciones
from Modelo.Cliente import Cliente

from Modelo.Trabajador import Trabajador
from Modelo.Camarero import Camarero as Camarero
from Modelo.Cocinero import Cocinero as Cocinero 

from Modelo.Producto import Producto
from Modelo.Comida import Comida
from Modelo.Bebida import Bebida


class Controlador:
    @staticmethod
    def flujo_menu_principal(opcion, plantilla, stock):
        if (opcion == 1):
            print("1 - Crear trabajador")
        elif (opcion == 2):
            print("2 - Crear producto")
        elif (opcion == 3):
            print("3 - Asignar cliente a camarero")
        elif (opcion == 4):
            print("4 - Modificar antigüedad")
        elif (opcion == 5):
            print("5 - Realizar pedido")
        elif (opcion == 6):
            print("6 - Tomar pedido")
        elif (opcion == 7):
            print("7 - Entregar pedido")
        elif (opcion == 8):
            print("8 - Preparar pedido")
        elif (opcion == 9):
            print("9 - Inventario con __dict__")
            Resultados.mostrar_listados(plantilla)
            Resultados.mostrar_listados(stock)
        elif (opcion == 0):
            return 0
        else:
            print("Hay algo que no está funcionando como sería deseable.")

        Menus_Salidas.borrado_vuelta_menu_principal()

    @staticmethod
    def crear_trabajador(tipo, trabajador):

        dni_valido = Validaciones.validar_dni(trabajador["dni"])
        print(dni_valido)
        while (dni_valido == False):
            trabajador["dni"] = Introducciones.reiterar_entrada("DNI")
            dni_valido = Validaciones.validar_dni(trabajador["dni"])

        if (tipo == 1):
            nuevo_trabajador = Camarero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"], trabajador["lista_clientes"])
        else:
            nuevo_trabajador = Cocinero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"])

        #plantilla.append(nuevo_trabajador)

        return nuevo_trabajador
    
    def crear_producto(tipo, producto):
        '''
        dni_valido = Validaciones.validar_dni(trabajador["dni"])
        print(dni_valido)
        while (dni_valido == False):
            trabajador["dni"] = Introducciones.reiterar_entrada("DNI")
            dni_valido = Validaciones.validar_dni(trabajador["dni"])

        if (tipo == 1):
            nuevo_trabajador = Camarero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"], trabajador["lista_clientes"])
        else:
            nuevo_trabajador = Cocinero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"])

'''
        nuevo_producto = Comida(producto["nombre"],producto["precio"],producto["tipo"],producto["ingredientes"])
        return nuevo_producto

    def crear_cliente(cliente):
        pass