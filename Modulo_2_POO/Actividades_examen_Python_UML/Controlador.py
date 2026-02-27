
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
        while (dni_valido == False):
            trabajador["dni"] = Introducciones.reiterar_entrada("DNI")
            dni_valido = Validaciones.validar_dni(trabajador["dni"])

        sueldo_valido = Validaciones.validar_float(trabajador["sueldo"])
        while (sueldo_valido == False):
            trabajador["sueldo"] = Introducciones.reiterar_entrada ("sueldo")
            sueldo_valido = Validaciones.validar_float(trabajador["sueldo"])

        if (tipo == 1):
            nuevo_trabajador = Camarero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"], trabajador["lista_clientes"])
        else:
            nuevo_trabajador = Cocinero(trabajador["nombre"], trabajador["dni"],trabajador["sueldo"])

        return nuevo_trabajador
    

    def crear_producto(tipo, producto):
        # Validar precio
        precio_validado = Validaciones.validar_float(producto["precio"])
        while (precio_validado == False):
            producto["precio"] = Introducciones.reiterar_entrada("PRECIO")
            precio_validado = Validaciones.validar_float(producto["precio"])

        if (tipo == 1):
            nuevo_producto = Comida(producto["nombre"],producto["precio"],producto["tipo"],producto["ingredientes"])
        else:
            # Validar tamaño
            tamanyo_validado = Validaciones.validar_float(producto["tamanyo"])
            while (tamanyo_validado == False):
                producto["tamanyo"] = Introducciones.reiterar_entrada("TAMAÑO")
                tamanyo_validado = Validaciones.validar_float(producto["tamanyo"])

            # Validar temperatura
            temperatura_validado = Validaciones.validar_float(producto["temperatura"])
            while (temperatura_validado == False):
                producto["temperatura"] = Introducciones.reiterar_entrada("TEMPERATURA")
                temperatura_validado = Validaciones.validar_float(producto["temperatura"])
            nuevo_producto = Bebida(producto["nombre"],producto["precio"],producto["tamanyo"],producto["temperatura"])
        return nuevo_producto


    def escoger_cliente(clientes):
        # Pedir y validar el cliente
        num_cliente = Introducciones.seleccionar_persona(clientes, "Cliente")
        num_cliente_validado = Validaciones.validar_numero_en_rango(num_cliente, len(clientes))
        while (num_cliente_validado == -1):
            num_cliente = Introducciones.reiterar_entrada("número de cliente")
            num_cliente_validado = Validaciones.validar_numero_en_rango(num_cliente, len(clientes))

        #cliente_escogido = []
        for i, objeto_cliente in enumerate(clientes):
            if (i+1 == num_cliente_validado):
                #print(objeto_cliente.nombre)
                return objeto_cliente

        
    def escoger_camarero(plantilla):
        # Formar lista camareros
        plantilla_camareros = []
        for camarero in plantilla:
            if (type(camarero) == Camarero):
                plantilla_camareros.append(camarero)

        # Pedir y validar el camarero
        num_camarero = Introducciones.seleccionar_persona(plantilla_camareros, "Camarero")

        num_camarero_validado = Validaciones.validar_numero_en_rango(num_camarero, len(plantilla_camareros))
        while (num_camarero_validado == -1):
            num_camarero = Introducciones.reiterar_entrada("número de camarero")
            num_camarero_validado = Validaciones.validar_numero_en_rango(num_camarero, len(plantilla_camareros))
        #camarero_escogido = []
        for i, objeto_camarero in enumerate(plantilla_camareros):
            if (i+1 == num_camarero_validado):
                return objeto_camarero


    def escoger_producto(stock):
        # Pedir y validar el producto
        num_producto = Introducciones.seleccionar_persona(stock, "Producto")
        num_producto_validado = Validaciones.validar_numero_en_rango(num_producto, len(stock))
        #cliente_escogido = []
        for i, objeto_producto in enumerate(stock):
            if (i+1 == num_producto_validado):
                #print(objeto_cliente.nombre)
                return objeto_producto


    def escoger_individuo(grupo):
        # Pedir y validar el individuo
        num_individuo = Introducciones.seleccionar_persona(grupo, 'uno de la lista: ')
        num_individuo_validado = Validaciones.validar_numero_en_rango(num_individuo, len(grupo))
        #individuo_escogido = []
        for i, objeto_individuo in enumerate(grupo):
            if (i+1 == num_individuo_validado):
                #print(f'ESCOGIDO: {objeto_individuo.nombre}')
                return objeto_individuo


    def ejecutar_cambio_fecha(operacion, persona):
        if (operacion == 1):
            #print(f'ALTA: {persona.nombre}')
            persona.dar_de_alta()
        elif (operacion == 2):
            #print(f'BAJA: {persona.nombre}')
            persona.dar_de_baja()
        elif(operacion == 3):
            antiguedad = persona.antiguedad()
            print (f'La antiguedad de {persona.nombre} es de {antiguedad} días')


    def preparar_pedido():
        unidades = Introducciones.introducir_entero(" de unidades")
        unidades_validadas = Validaciones.validar_numero_en_rango(unidades,100)
        while (unidades_validadas == -1):
            unidades = Introducciones.reiterar_entrada("numero entero de unidades inferior a 101")
            unidades_validadas = Validaciones.validar_numero_en_rango(unidades,100)
        return unidades_validadas