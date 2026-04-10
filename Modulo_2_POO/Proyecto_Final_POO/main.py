import os

#Controlador
from Controlador.controlador_juego import iniciar_juego

#Modelo
from Modelo.validaciones import Validaciones

#Vista
from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus



def main():
    os.system("cls")
    print(Mensajes.TITULO)
    
    interfaz = Menus.menu(Menus.menu_interfaz)
    
    while True:
        if (interfaz == 1):
            print("GUI")
            break
        elif (interfaz == 2):
            print("GUI")
            break
        else:
            print("Adiós")
            break
    iniciar_juego()

if __name__ == "__main__":
    main()