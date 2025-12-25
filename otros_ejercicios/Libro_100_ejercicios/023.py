# ENUNCIADO Ejercicio 23: Utilización del método format()
# Escribir un programa que permita formatear la cadena de caracteres:
# "Me llamo miNombre y tengo edad años. Estoy aprendiendo el lenguaje Lenguaje".
# El programa debe permitir formatear esta cadena asignándole el contenido 
# de las variables a continuación:
# miNombre = "Julián" , edad = 32, Lenguaje = "Python"

# El programa debe mostrar en la consola: 
# "Me llamo Julian y tengo 32 años. Estoy aprendiendo el lenguaje Python"

import os, modulo as md
os.system("cls")
num_programa = 23

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