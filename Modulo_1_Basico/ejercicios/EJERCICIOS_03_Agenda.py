#PARA EJECUTAR SIN PROBLEMA, desde el directorio del módulo:
#python -m ejercicios.EJERCICIOS_03_Agenda


from ejercicios.EJERCICIOS_03_Agenda_Modulo import *
import os
os.system("cls")



# Función principal: muestra y llama al menú
def main():
    operacion = validar_menu_principal()
    if (operacion == 6):
        print(f"Hasta pronto\n{fin}")
        return
    elif (operacion == 5):
        print(agenda)
    elif (operacion == 1):
        anadir_contacto()
    elif (operacion == 2):
        consultar_contacto()
    elif (operacion == 3):
        modificar_contacto()
    elif (operacion == 4):
        borrar_contacto()
    main()

'''
# ¿OTRA OPERACIÓN?
def otra_operacion():
    otra = input("¿Desea realizar otra operación? [S/N]: ").lower()
    while True:
        if (otra == "s"):
            validar_menu_principal()
        elif (otra == "n"):
            print(fin)
            break
        else:
            otra = input("¿Cómo dice? [S/N]: ").lower()
'''


main()