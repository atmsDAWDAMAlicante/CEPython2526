# ENUNCIADO Ejercicio 25: 
# Escribir un programa que muestre la carpeta en la que se encuentra 
# el script de Python actual.

import os, modulo as md
os.system("cls")
num_programa = 25

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