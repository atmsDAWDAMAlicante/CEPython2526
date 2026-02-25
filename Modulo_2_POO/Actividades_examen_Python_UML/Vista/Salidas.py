
import os
from Modelo.Validaciones import Validaciones

class Menus_Salidas:
    @staticmethod
    def mostrar_menu_principal(menu):
        for i in menu:
            print(i)

    @staticmethod
    def fin_del_programa():
        print("\n\n","="*30," Fin del programa")


    @staticmethod
    def borrado_vuelta_menu_principal():
        print("\n\n","="*100)
        input("Operacion finalizada. Pulsa Intro para borrar la consola y volver al menú principal\n")
        Resultados.borrar_consola()

class Resultados:
    @staticmethod
    def borrar_consola():
        os.system("cls")

    @staticmethod
    def mostrar_listados(listado):
        print("\n\n","="*100)
        for i in listado:
            print(f'{type(i).__name__}: {i.__dict__}')

        '''
        if isinstance(i,Camarero):
            print(f'Camarero: {i.nombre}')
        else:
            print(f'{type(i).__name__}: {i.nombre}')
        '''

    @staticmethod
    def verificar_datos_objetos_creados(grupo):
        print("Verificación DNI plantilla existente:")
        for i in grupo:
            if ((Validaciones.validar_dni(i.get_dni())) == False):
                resultado = "INCORRECTO"
            else:
                resultado = "CORRECTO"
            print(f'Trabajador {i.nombre} - DNI: {i.get_dni()} es: {resultado}')
            

    