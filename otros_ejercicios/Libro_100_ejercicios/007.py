# ENUNCIADO Ejercicio 7: 
# Escribir un programa que solicite al usuario su edad y la almacene en
# una variable. El programa debe verificar si el usuario tiene una edad
# mayor o menor que 18 años. Si la edad del usuario es mayor o igual a 18, 
# entonces el programa debe imprimir 'El usuario es mayor de edad',
# de lo contrario debe imprimir 'El usuario es menor de edad'.

import os, modulo as md
os.system("cls")
num_programa = 7

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