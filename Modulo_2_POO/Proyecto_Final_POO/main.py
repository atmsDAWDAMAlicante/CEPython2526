import os

from Modelo.validaciones import Validaciones

from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus



def main():
    os.system("cls")
    print(Mensajes.TITULO)
    
    interfaz = Menus.menu(Menus.menu_interfaz)
    
    while True:
        if (interfaz == 1):
            print("CLI")
            break
        elif (interfaz == 2):
            print("GUI")
            break
        else:
            print("Adiós")
            break

if __name__ == "__main__":
    main()