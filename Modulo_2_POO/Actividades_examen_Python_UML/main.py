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
from Vista.Salidas import Menus_Salidas, Resultados

# Importar Controlador
from Controlador import Controlador


# Variables

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
plantilla = []
stock = []
clientes = []

def constructor_inicial():
    print("="*70,"\n","="*10,"GESTOR DE TRABAJADORES, STOCK Y CLIENTES","="*10,"\n","="*70)
    print("Previo: ejecución del método estático saludar del enunciado Actividad 2")
    Estatico.saludar()
    print("\n","-"*20,"A) CONSTRUCTOR TRABAJADORES")
    # Plantilla inicial
    plantilla.append(Camarero("Pepe Pérez Pérez", "1111111A", 1205.32, []))
    plantilla.append(Camarero("Manolo Martínez Martínez", "22222222B", 1132.45, []))
    plantilla.append(Cocinero("Luisa López López", "33333333C", 1300.45))
    plantilla.append(Cocinero("Francisca Fernández Fernández", "44444444D", 1700.20))
    Resultados.mostrar_listados(plantilla)
    
    print("-"*20,"B) CONSTRUCTOR STOCK")
    # Stock inicial
    stock.append(Bebida("Coca Cola", "Grande", "Fria", 1.2))
    stock.append(Bebida("Agua mineral", "Pequeña", "Natural", 0.5))
    stock.append(Comida("Patatas fritas", 1.5, "Snack", "Patatas, aceite y sal"))
    stock.append(Comida("Nocilla", 3.4, "Postre", "Leche-cacao-avellanas-azucar"))
    Resultados.mostrar_listados(stock)
    print("-"*20,"C) CONSTRUCTOR CLIENTES")
    # Stock inicial
    Resultados.mostrar_listados(clientes)

    Menus_Salidas.borrado_vuelta_menu_principal()

class Estatico:
    @staticmethod
    def saludar():
        print("Hola")
        

def flujo_menu_principal(opcion):
    if (opcion == 1):
        tipo = Introducciones.seleccionar_tipo_trabajador()
        tipo_validado = Validaciones.validar_numero_en_rango(tipo, 2)
        while (tipo_validado == -1):
            tipo = Introducciones.reiterar_entrada("tipo de trabajador: 1-Camarero / 2-Cocinero")
            print(tipo_validado)
            tipo_validado = Validaciones.validar_numero_en_rango(tipo,2)
        print(tipo_validado)
        #plantilla.append(Introducciones.crear_trabajador(tipo_validado))
        trabajador = Introducciones.introducir_datos_trabajador(tipo_validado)
        plantilla.append(Controlador.crear_trabajador(tipo_validado, trabajador))


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
        Resultados.mostrar_listados(plantilla)
        Resultados.mostrar_listados(stock)
    else:
        print("Hay algo que no está funcionando como sería deseable.")

    Menus_Salidas.borrado_vuelta_menu_principal()





def main():
    os.system("cls")
    constructor_inicial()

    while True:
        Menus_Salidas.mostrar_menu_principal(menu_principal)
        opcion_principal = Validaciones.validar_menu_principal(Menus_Entradas.optener_op_menu_principal(menu_principal))
        if opcion_principal == 0:
            Menus_Salidas.fin_del_programa()
            break
        elif (opcion_principal == -1):
            print(f'MAL {opcion_principal}')
        else:
            flujo_menu_principal(opcion_principal)
        












  

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