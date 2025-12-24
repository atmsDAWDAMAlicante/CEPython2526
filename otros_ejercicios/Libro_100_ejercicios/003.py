# ENUNCIADO Ejercicio 3: 
# Escribir una serie de instrucciones de Python que permita declarar 2
# variables 'x' e 'y' asignándoles respectivamente los valores 3 y 8.5, luego
# convertir el tipo de estas variables a una cadena de caracteres.
# Al final, el programa debe mostrar el tipo de estas variables después de
# la conversión.

import os, modulo as md
os.system("cls")
num_programa = 3


# Modelo
def conversion_a_cadena(x, y):
    # Conversión de las variables a cadena
    x = str(x)
    y = str(y)
    return x, y

# Vista
def mostrar_inicio():
    md.mostrar_inicio(num_programa)
def mostrar_final():
    md.mostrar_final()

def mostrar_tipos(x, y):
    print("Ejercicio 3:")
    print(f"Tipo de la variable 'x' después de la conversión: {type(x)}")
    print(f"Tipo de la variable 'y' después de la conversión: {type(y)}")

# Controlador
def main():
    mostrar_inicio()
    # Declaración de las variables x e y
    x = 3
    y = 8.5
    # Llamada a la función conversión a cadena
    x, y = conversion_a_cadena(x, y)
    # Mostrar el tipo de las variables convertidas
    mostrar_tipos(x, y)
    mostrar_final()

if __name__ == "__main__":
    main()