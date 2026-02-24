class Introducciones:
    @staticmethod
    def crear_trabajador(tipo):
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
    def reiterar_entrada():
        dato = input("Introduce el dato correctamente: ")
        return dato

class Menus_Entradas:
    @staticmethod
    def mostrar_menu_principal(menu):
        for i in menu:
            print(i)
        return input("Seleccione una operación: ")