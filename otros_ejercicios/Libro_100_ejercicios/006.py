# ENUNCIADO Ejercicio 6: 
# Escribir un programa que declare la variable "d" y le asigne el valor 5, y
# verifique si esta variable es mayor o menor que 0. Si la variable es
# mayor que 0, el programa debe imprimir 'Positiva', de lo contrario debe
# imprimir 'Negativa'.

import os, modulo as md
os.system("cls")
num_programa = 6

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