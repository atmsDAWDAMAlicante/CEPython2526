import os

#Controlador
from Controlador.controlador_juego import Controlador_juego

#Modelo
from Modelo.validaciones import Validaciones

#Vista
from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus, Vista_CLI
from Vista.vista_gui import Vista_GUI



def main():
    os.system("cls")
    print(Mensajes.TITULO)
    
    interfaz = Menus.menu(Menus.menu_interfaz)
    
    while True: # Bucle provisional ---- ES PROVISIONAL
        if (interfaz == 1):
            vista = Vista_CLI()
            break
        elif (interfaz == 2):
            #vista = Vista_GUI()
            print("¡¡¡En obras: GUI!!!")
            break
        else:
            print("Adiós")
            break
    controlador = Controlador_juego(vista)
    controlador.iniciar_juego()

if __name__ == "__main__":
    main()