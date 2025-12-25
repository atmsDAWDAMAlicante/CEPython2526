# ENUNCIADO Ejercicio 30: Generar aleatoriamente un número
# Escribir un programa para generar aleatoriamente un número entre 20 y 30.

import os, modulo as md
os.system("cls")
num_programa = 30

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