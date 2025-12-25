# ENUNCIADO Ejercicio 9: Números impares incluidos en un intervalo
# Escribir un programa en Python que permita imprimir solo los números
# impares entre 10 y 20.
# Nota: es necesario crear dos versiones, una con el bucle for y otra con el bucle while.

import os, modulo as md
os.system("cls")
num_programa = 9

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