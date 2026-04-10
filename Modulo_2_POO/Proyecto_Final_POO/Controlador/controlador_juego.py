from Vista.vista_cli import Menus


class Controlador_juego:
    def __init__(self, vista1):
        self.vista = vista1

    def iniciar_juego():
        print(f"Dentro del {self.vista1}")

        while True:

            opcion = Menus.menu_principal(Menus.menu_iniciar_juego)

            if opcion == 1:
                self.nueva_partida()

            elif opcion == 2:
                #self.cargar_partida()
                pass
            elif opcion == 0:
                self.vista.mostrar("Hasta pronto")
                break
    def nuevo_juego():
        print("EMPEZAMOS")
    def cargar_partida():
        print("Selecciona el archivo JSON")
    