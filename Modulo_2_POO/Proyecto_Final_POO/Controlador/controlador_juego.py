from Vista.vista_cli import Vista_CLI


class Controlador_juego:

    def __init__(self, vista):
        self.vista = vista

    def iniciar_juego(self):
        print(f"Dentro del {self.vista}")

        while True:

            opcion = self.vista.menu_iniciar_juego()

            if opcion == 1:
                self.nuevo_juego()

            elif opcion == 2:
                self.guardar_partida()

            elif opcion == 0:
                self.vista.imprimir_mensaje("Adiós")
                break

    def nuevo_juego(self):
        self.vista.imprimir_mensaje("Empezamos el juego")

    def guardar_partida(self):
        self.vista.imprimir_mensaje("Partida guardada")
    