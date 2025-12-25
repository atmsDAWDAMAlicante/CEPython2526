# ENUNCIADO Ejercicio 28: 
# Escribir un programa que permita calcular el tiempo de ejecución de un script.
# Tomaremos como ejemplo el script del ejercicio 24 y calcularemos su tiempo de ejecución.
# El programa debe mostrar al final la tabla de multiplicación 
# del ejercicio 24 junto con el tiempo de ejecución.

import os, modulo as md
os.system("cls")
num_programa = 28

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