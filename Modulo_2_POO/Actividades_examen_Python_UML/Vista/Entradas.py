class Introducciones:
    # Plantilla
    @staticmethod
    def seleccionar_tipo_trabajador():
        return input("Introduce el tipo de trabajador: 1-Camarero / 2-Cocinero")

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
    def reiterar_entrada(tipo):
        dato = input(f"Introduce el {tipo} correctamente: ")
        return dato

class Menus_Entradas:
    @staticmethod
    def optener_op_menu_principal(menu):
        return input("Seleccione una operación: ")