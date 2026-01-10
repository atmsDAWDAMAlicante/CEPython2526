import os
import decimal
from modelo import Empleado, empresa, Validaciones
from vista import Introduccion, Impresion

os.system('cls')
mensaje_inicio_programa = "=== Inicio del programa ==="
mensaje_fin_programa = "=== Fin del programa ==="

def main(): # Inicio del programa: menú principal
    Impresion.impresion_basica(mensaje_inicio_programa)
    while True:
        Impresion.impresion_basica("Seleccione una opción:")
        num = Introduccion.introducir_operacion(f'1.- Cambiar departamento\n2.- Calculo nómina/horas extra\n3.- Info completa\n\n0.- Salir: ---> ')
        operacion = Validaciones.validar_enteros(num)
        if (operacion != -1):
            if (operacion == 1):
                Impresion.impresion_basica("Cambiar departamento")
            elif (operacion == 2):
                Impresion.impresion_basica("Calculo nomina")
            elif (operacion == 3):
                Impresion.impresion_basica("Info")
            else:
                Impresion.impresion_basica(mensaje_fin_programa)
                break

if __name__ == "__main__":
    main()


