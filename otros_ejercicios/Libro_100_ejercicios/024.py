# ENUNCIADO Ejercicio 24: 
# Escribir un programa que muestre la tabla de multiplicación del número 8.
# El programa debe devolver la siguiente salida:
# 8x0=0
# 8x1=8
# 8x2=16
# 8x3=24
# 8x4= 32
# 8x5=40
# 8x6= 48
# 8x7=56
# 8x8= 64
# 8x9=72
# 8x10=80

import os, modulo as md
os.system("cls")
num_programa = 24

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