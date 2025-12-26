# ENUNCIADO Ejercicio 6: 
# Escribir un programa que declare la variable "d" y le asigne el valor 5, y
# verifique si esta variable es mayor o menor que 0. Si la variable es
# mayor que 0, el programa debe imprimir 'Positiva', de lo contrario debe
# imprimir 'Negativa'.

import os, modulo as md
os.system("cls")
num_programa = 6

# Modelo
def validar_numero(func):
    def envoltura(num):
        try:
            valor = int(num)
        except ValueError:
            return "Error"
        else:
            return func(valor)
    return envoltura

@validar_numero
def verificar_numero(num):
    num = int(num)
    if num > 0:
        return "Positiva"
    elif num < 0:
        return "Negativa"
    else:
        return "Error"

# Vista
def mostrar_inicio():
    md.mostrar_inicio(num_programa)
def mostrar_final():
    md.mostrar_final()
def pide_numero():
    num = input("Introduce un número entero: ")
    return num
def imprimir_resultado(resultado):
    print(resultado)

# Controlador
def main():
    mostrar_inicio()
    num = pide_numero()
    resultado = verificar_numero(num)
    imprimir_resultado(resultado)
    mostrar_final()

if __name__ == "__main__":
    main()  