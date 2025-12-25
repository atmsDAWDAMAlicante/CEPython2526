# ENUNCIADO Ejercicio 10: Comprensión de listas
# Escribir una instrucción que permita crear una lista de números del 1 al 10 
# utilizando una comprensión de lista.

import os, modulo as md
os.system("cls")
num_programa = 10

# Modelo


# Vista
def mostrar_inicio():
    md.mostrar_inicio(num_programa)
def mostrar_final():
    md.mostrar_final()

# Controlador
def main():
    mostrar_inicio()
    # Aquí va la lógica del programa
    mostrar_final()

if __name__ == "__main__":
    main()  