#PARA EJECUTAR SIN PROBLEMA, desde el directorio del módulo:
#python -m ejercicios.EJERCICIOS_03_Agenda


from ejercicios.EJERCICIOS_03_Agenda_Modulo import *
import os
os.system("cls")



# Función principal: muestra y llama al menú
def main():
    operacion = validar_menu()
    if (type(operacion) == int):
        ejecutar_operacion(operacion)
main()