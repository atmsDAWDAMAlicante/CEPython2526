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
    "3 - Fechas: altas, bajas, antigüedad",
    "4 - Asignar cliente a camarero",
    "5 - Realizar pedido",
    "6 - Inventario con __dict__",
    "7 - Salir"
]
plantilla = []
stock = []
clientes = []

def constructor_inicial():
    print("="*70,"\n","="*10,"GESTOR DE TRABAJADORES, STOCK Y CLIENTES","="*10,"\n","="*70)

    # PRIMERA ACTIVIDAD: MÉTODO ESTÁTICO SALUDAR
    print("Previo: ejecución del método estático saludar del enunciado Actividad 2")
    Estatico.saludar()

    # CREAR Y MOSTRAR LOS OBJETOS TRABAJADOR, LA VALIDACION DE LOS ATRIBUTOS DNI y PASSWORD y MOSTRAR ANTIGÜEDAD
    print("\n","-"*20,"A) CONSTRUCTOR TRABAJADORES:")
    # Plantilla inicial
    plantilla.append(Camarero("Pepe Pérez Pérez", "123456A", 1205.32, []))
    plantilla.append(Camarero("Manolo Martínez Martínez", "12345678B", 1132.45, []))
    plantilla.append(Cocinero("Luisa López López", "12345678C", 1300.45))
    plantilla.append(Cocinero("Francisca Fernández Fernández", "12345678D", 1700.20))
    plantilla[0].password = "abc"
    print("A.1 - Impresión del resultado de la verificación de los campos DNI y password:")
    Resultados.verificar_datos_objetos_creados(plantilla)
    # Se muestra la antigüedad de los trabajadores, calculada por un método de la clase padre (no es un atributo)
    print("-"*50,"\nA.2 - Se muestra la antigüedad de cada uno calculada (no es un atributo de la clase):")
    for i in plantilla:
        print(f'Antigüedad del {type(i)} {i.nombre}: {i.antiguedad()} días (alta: {i.fecha_alta} / baja: {i.fecha_baja})')

    print("-"*50,"\nA.3 - RESULTADO: detalle de los objetos trabajador (CAMARERO y COCINERO) y sus atributos modificados:")
    Resultados.mostrar_listados(plantilla)

    # CREAR Y MOSTRAR LOS OBJETOS PRODUCTO
    print("-"*20,"B) CONSTRUCTOR STOCK:")
    # Stock inicial
    stock.append(Bebida("Coca Cola", 1.80, 0.5, 0.9))
    stock.append(Bebida("Agua mineral", 0.5, 0.33, 1.5))
    stock.append(Comida("Patatas fritas", 1.5, "Snack", "Patatas, aceite y sal"))
    stock.append(Comida("Nocilla", 3.4, "Postre", "Leche-cacao-avellanas-azucar"))
    Resultados.mostrar_listados(stock)

    # CREAR Y MOSTRAR LOS OBJETOS CLIENTE
    print("-"*20,"C) CONSTRUCTOR CLIENTES:")
    # Clientes inicial
    clientes.append(Cliente("Ana"))
    clientes.append(Cliente("Juan"))
    clientes.append(Cliente("Victor"))
    Resultados.mostrar_listados(clientes)


    # CREAR Y MOSTRAR LOS OBJETOS CLIENTE
    print("-"*20,"D) PEDIDOS: realización y resultados:")
    # Realización de los pedidos
    # Pedido específico: cliente 3 a camarero 2
    print(f"D.1 - Pedido específico: cliente 3 '{clientes[2].nombre}' hace pedido (Coca cola) a camarero 2 '{plantilla[1].nombre}'")
    plantilla[1].lista_clientes.append(clientes[2].nombre)
    clientes[2].realizar_pedido(stock[0],plantilla[1],5)
    print(plantilla[1].__dict__)
    print(clientes[2].__dict__)
    Menus_Salidas.borrado_vuelta_menu_principal()

class Estatico:
    @staticmethod
    def saludar():
        print("Hola")
        

def flujo_menu_principal(opcion):
    if (opcion == 1):
        # Selección del tipo de trabajador a introducir y validación
        # 1-Camarero / 2-Cocinero
        tipo = Introducciones.seleccionar_tipo_trabajador()
        tipo_validado = Validaciones.validar_numero_en_rango(tipo, 2)
        while (tipo_validado == -1):
            tipo = Introducciones.reiterar_entrada("tipo de trabajador: 1-Camarero / 2-Cocinero:  ")
            tipo_validado = Validaciones.validar_numero_en_rango(tipo,2)

        # Introducción de datos para crear el objeto del tipo de trabajador seleccionado
        trabajador = Introducciones.introducir_datos_trabajador(tipo_validado)

        # Inclusión del objeto creado (se llama al Controlador) a la lista "plantilla"
        plantilla.append(Controlador.crear_trabajador(tipo_validado, trabajador))


    elif (opcion == 2):
        # Selección del tipo de producto a introducir y validación
        # 1-Comida / 2-Bebida
        tipo = Introducciones.seleccionar_tipo_producto()
        tipo_validado = Validaciones.validar_numero_en_rango(tipo, 2)
        while (tipo_validado == -1):
            tipo = Introducciones.reiterar_entrada("tipo de producto: 1-Comida / 2-Bebida:  ")
            tipo_validado = Validaciones.validar_numero_en_rango(tipo,2)

        # Introducción de datos para crear el objeto del tipo de producto seleccionado
        producto = Introducciones.introducir_datos_producto(tipo_validado)
        # Inclusión del objeto creado (se llama al Controlador) a la lista "stock"
        stock.append(Controlador.crear_producto(tipo_validado, producto))



    elif (opcion == 3):
        #3 - Fechas: altas, bajas, antigüedad
        tipo = Introducciones.seleccionar_grupo()
        tipo_validado = Validaciones.validar_numero_en_rango(tipo, 2)
        while (tipo_validado == -1):
            tipo = Introducciones.reiterar_entrada("Seleccione correctamente: 1 - Trabajador / 2 - Cliente: ")
            tipo_validado = Validaciones.validar_numero_en_rango(tipo,2)
        if (tipo_validado == 1):
            persona = Controlador.escoger_individuo(plantilla)
        else:
            persona = Controlador.escoger_individuo(clientes)
        
        tipo_operacion = Introducciones.reiterar_entrada("Seleccione: 1 - Alta / 2 - Baja / 3 - Ver antigüedad: ")
        tipo_operacion_validado = Validaciones.validar_numero_en_rango(tipo_operacion,3)
        while (tipo_operacion_validado == -1):
            tipo_operacion = Introducciones.reiterar_entrada("Seleccione correctamente: 1 - Alta / 2 - Baja / 3 - Ver antigüedad: ")
            tipo_operacion_validado = Validaciones.validar_numero_en_rango(tipo_operacion,3)

        Controlador.ejecutar_cambio_fecha(tipo_operacion_validado, persona)



    elif (opcion == 4):
        print("4 - Asignar cliente a camarero")
        cliente_seleccionado = Controlador.escoger_cliente(clientes)
        print(f'CLIENTE {cliente_seleccionado.nombre}')
        camarero_seleccionado = Controlador.escoger_camarero(plantilla)
        camarero_seleccionado.lista_clientes.append(cliente_seleccionado.nombre)
        print(f'Lista de clientes del camarero {camarero_seleccionado.nombre}: ')
        for i in camarero_seleccionado.lista_clientes:
            print(f'{i}')
            pass


    elif (opcion == 5):
        print("5 - Realizar pedido")
        cliente_seleccionado = Controlador.escoger_cliente(clientes)
        print(f'CLIENTE {cliente_seleccionado.nombre}')
        camarero_seleccionado = Controlador.escoger_camarero(plantilla)
        producto_seleccionado = Controlador.escoger_producto(stock)
        unidades = Controlador.preparar_pedido()
        
        # Método de la clase Cliente para realizar el pedido
        cliente_seleccionado.realizar_pedido(producto_seleccionado, camarero_seleccionado, unidades)
        


    elif (opcion == 6):
        Resultados.mostrar_listados(plantilla)
        Resultados.mostrar_listados(stock)
        Resultados.mostrar_listados(clientes)

    #else:
     #   print("Hay algo que no está funcionando como sería deseable.")

    Menus_Salidas.borrado_vuelta_menu_principal()





def main():
    os.system("cls")
    constructor_inicial()

    while True:
        Menus_Salidas.mostrar_menu_principal(menu_principal)
        opcion_principal = Validaciones.validar_menu_principal(Menus_Entradas.optener_op_menu_principal(menu_principal))
        if opcion_principal == 7:
            Menus_Salidas.fin_del_programa()
            break
        elif (opcion_principal == -1):
            print(f'MAL {opcion_principal}- Introduce un número entre 1 y 7')
            #opcion_principal = Validaciones.validar_menu_principal(Menus_Entradas.optener_op_menu_principal(menu_principal))
        else:
            flujo_menu_principal(opcion_principal)
        

if __name__ == "__main__":
    main()