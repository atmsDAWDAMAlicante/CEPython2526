
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
        print("="*100)
        for i in listado:
            print(f'{type(i).__name__}: {i.__dict__}')
        print("="*100)
        '''
        if isinstance(i,Camarero):
            print(f'Camarero: {i.nombre}')
        else:
            print(f'{type(i).__name__}: {i.nombre}')
        '''

    @staticmethod
    def verificar_datos_objetos_creados(grupo):
        print("Verificación DNI/Password de los integrantes de la plantilla actual:")
        for i in grupo:
            if ((Validaciones.validar_dni(i.get_dni())) == False):
                resultado_dni = "INCORRECTO"
            else:
                resultado_dni = "CORRECTO"
            if ((Validaciones.validar_password(i.password)) == False):
                resultado_password = "INCORRECTA"
            else:
                resultado_password = "CORRECTA"
            print(f'Del {type(i).__name__} {i.nombre} su DNI: {i.get_dni()} es {resultado_dni} y su password "{i.password}" es {resultado_password}')
        print("="*60,)
            

    