# ENUNCIADO Ejercicio 5: 
# Crear una serie de instrucciones en Python que permitan declarar una variable 
# "var" y asignarle el valor "Hola". Luego, el programa debe verificar 
# si la variable "var" es un entero o una cadena de caracteres.
# Si es un entero, el programa debe imprimir en la consola "Entero", 
# y si esuna cadena de caracteres, el programa debe imprimir "Cadena de
# caracteres" en la consola.

import os, modulo as md
os.system("cls")
num_programa = 5

# Modelo
def declarar_variable():
    var = "Hola"
    return var

def verificar_tipo(var):
    if type(var) == int:
        return "Entero"
    elif type(var) == str:
        return "Cadena de caracteres"
    else:
        return type(var)

# Vista
def mostrar_inicio():
    md.mostrar_inicio(num_programa)
def mostrar_final():
    md.mostrar_final()

def mostrar_tipo(tipo):
    print(f"{tipo}")

# Controlador

def main():
    mostrar_inicio()
    # Operaciones del Modelo
    var = declarar_variable()
    tipo = verificar_tipo(var)

    # Operaciones de la Vista
    mostrar_tipo(tipo)

    mostrar_final()

if __name__ == "__main__":
    main()