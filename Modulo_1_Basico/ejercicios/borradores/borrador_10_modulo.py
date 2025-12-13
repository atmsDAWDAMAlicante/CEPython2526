import random

menu = ["1-Añadir", "2-Ver","3-Algo", "4-Otro", "5-Otro","6-Salir"]
agenda = {{"Pepi" : {"apellido":"Garcia","telefono":"965000000"}},
          {"Luis" : {"apellido":"Lopez","telefono":"616000000"}}
          }

def ejecutar_menu():
    opcion = input(f'Elige una opcion{menu}')
    while True:
        try:
            opcion = int(opcion)
            if (opcion > 0 ) and (opcion < 7):
                ejecutar_opcion(opcion)
                break
            else:
                print("Intruduzca un número del 1 al 6")
        except ValueError:
            print(f'Introduzca un número entero del 1 al 6')
        opcion = input(f'Elige una opcion ¡¡¡PERO AHORA BIEN!!! {menu}')



def saludar():
    print("Hola")

def ejecutar_opcion(num):
    if (num == 6):
        print(f'Vd. ha seleccionado: {menu[num-1]}\nVuelva pronto')
    else: 
        print(f'Vd. ha seleccionado: {menu[num-1]}')

