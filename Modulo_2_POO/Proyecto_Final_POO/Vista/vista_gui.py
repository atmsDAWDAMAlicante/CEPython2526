# Ya haré algo aquí después para la interfaz GUI

from Vista.vista_cli import Vista_CLI

import tkinter as tk


class Vista_GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RPG")

        # LOG
        self.label = tk.Label(self.root, text="", justify="left", anchor="w")
        self.label.pack(padx=10, pady=10)

        # BOTONES
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.opcion = None
        self.var = tk.IntVar()

    def imprimir_mensaje(self, mensaje):
        self.label.config(text=self.label.cget("text") + "\n" + mensaje)

    def limpiar_botones(self):
        for w in self.frame.winfo_children():
            w.destroy()

    def crear_botones(self, opciones):
        self.limpiar_botones()
        self.opcion = None
        self.var.set(0)

        for texto, valor in opciones:
            b = tk.Button(self.frame, text=texto,
                          command=lambda v=valor: self.seleccionar(v))
            b.pack(pady=2)

        self.root.wait_variable(self.var)

    def seleccionar(self, valor):
        self.opcion = valor
        self.var.set(1)

    # -------- MENÚS --------

    def menu_iniciar_juego(self):
        self.imprimir_mensaje("Menú principal")

        self.crear_botones([
            ("Nuevo juego", 1),
            ("Guardar", 2),
            ("Continuar", 3),
            ("Cargar", 4),
            ("Salir", 0)
        ])

        return self.opcion

    def menu_elegir_jugador(self, lista):
        self.imprimir_mensaje("Elige personaje")

        opciones = [(nombre, i+1) for i, nombre in enumerate(lista)]

        self.crear_botones(opciones)
        return self.opcion

    def menu_combate(self):
        self.crear_botones([
            ("Ataque", 1),
            ("Ataque cargado", 2),
            ("Poción", 3),
            ("Kame", 4),
            ("Salir", 0)
        ])

        return self.opcion

    def iniciar(self):
        self.root.mainloop()