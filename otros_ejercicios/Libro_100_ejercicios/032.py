# ENUNCIADO Ejercicio 32: 
# Escribir un programa que cree una variable L y le asigne la lista [3,6,9,12,15,18,21,24].
# Luego, crear una nueva lista L1 mediante una comprensión de lista 
# que contenga los números de L divididos por 3.
# 
# El programa debe mostrar la lista L1 en la consola.

import os, modulo as md
os.system("cls")
num_programa = 32

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