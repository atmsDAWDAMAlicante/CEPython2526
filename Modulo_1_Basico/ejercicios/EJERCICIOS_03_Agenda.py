
from ejercicios.EJERCICIOS_03_Agenda_Modulo import *
import os
os.system("cls")

# Menú principal
def main():
    operacion = validar_menu(input("Introduce una operacion: "))
    while True:
        if (operacion == -1):
           operacion = validar_menu(input("Introduce una operacion, PERO AHORA HAZLO BIEN: "))
        else:
            print(f'Has elegido: {operacion}')
            a = ejecutar_operacion(operacion)
            print(a)
            formar_diccionario()
            break
        
main()