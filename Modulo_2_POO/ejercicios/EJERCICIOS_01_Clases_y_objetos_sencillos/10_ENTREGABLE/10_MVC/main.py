import os
import decimal
from modelo import Empleado, empresa, Validaciones
from vista import Introduccion, Impresion

os.system('cls')

def main():
    print("=== Inicio del programa ===")
    while True:
        print("Seleccione una opción")
        num = Introduccion.introducir_operacion()
        operacion = Validaciones.validar_enteros(num)
        if (operacion != -1):
            Impresion.impresion_basica(f'Vd. ha introducido: {num}')
            break

if __name__ == "__main__":
    main()


