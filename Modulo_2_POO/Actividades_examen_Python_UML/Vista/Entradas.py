class Introducciones:
    # Plantilla
    @staticmethod
    def seleccionar_tipo_trabajador():
        return input("Introduce el tipo de trabajador: 1-Camarero / 2-Cocinero:  ")

    @staticmethod
    def introducir_datos_trabajador(tipo):
        trabajador = {"nombre": "", "dni": "", "sueldo": ""}
        trabajador["nombre"] = input("Introduce el nombre: ")
        trabajador["dni"] = input("Introduce el DNI: ")
        trabajador["sueldo"] = input("Introduce el sueldo: ")
        if (tipo == 1): # Camarero
            trabajador["lista_clientes"] = input("Introduce la Lista de Clientes: ")
        else: # Cocinero
            pass
        return trabajador
        
    @staticmethod
    def seleccionar_tipo_producto():
        return input("Introduce el tipo de trabajador: 1-Comida / 2-Bebida:  ")

    @staticmethod
    def introducir_datos_producto(tipo):
        producto = {"nombre": "", "precio": ""}
        producto["nombre"] = input("Introduce el nombre: ")
        producto["precio"] = input("Introduce el precio: ")
        if (tipo == 1): # Comida
            producto["tipo"] = input("Introduce el tipo de comida: ")
            producto["ingredientes"] = input("Introduce los ingredientes: ")
        else: # Bebida
            producto["tamanyo"] = input("Introduce el tamaño de la bebida: ")
            producto["temperatura"] = input("Introduce la temperatura de la bebida: ")
        return producto


    @staticmethod
    def reiterar_entrada(tipo):
        dato = input(f"Introduce el {tipo} correctamente: ")
        return dato
    

    @staticmethod
    def seleccionar_persona(lista, tipo):
        print(f"Selecciona el {tipo}:")
        contador = 1
        for i in lista:
            print(f'{contador} - {i.nombre}')
            contador +=1
        return (input(f'Seleccione el nº de {tipo}: '))
    
    @staticmethod
    def introducir_fecha():
        fecha = input("Introduce una fecha válida (aaaa-mm-dd): ")
        return fecha 







class Menus_Entradas:
    @staticmethod
    def optener_op_menu_principal(menu):
        return input("Seleccione una operación: ")
    
