# ENUNCIADO Ejercicio 31: Visualización de motivos
# Escribir un programa que muestre los siguientes números en la consola:
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

import os, modulo as md
os.system("cls")
num_programa = 31

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