#ENUNCIADO Ejercicio 2: 
# Escribir una secuencia de instrucciones de Python 
# que permita declarar una variable llamada ch inicializándola 
# con el valor 'hola' y luego modificar esa misma variable para 
# que contenga el mensaje 'está bien' .
# El programa debe mostrar el contenido de la variable en la consola 
#después de la modificación.

import os, modulo as md
os.system("cls")
num_programa = 2


# Modelo
def modificar_variable(ch):
    ch = "está bien"  # Modifica el valor de la variable ch
    return ch
    
# Vista
def mostrar_inicio():
    md.mostrar_inicio(num_programa)
def mostrar_final():
    md.mostrar_final()

def mostrar_variable(ch):
    print("Ejercicio 2:")
    print(f"Contenido de la variable 'ch' después de la modificación: '{ch}'")

# Controlador
def main():
    mostrar_inicio()
    ch = "hola"  # Inicializa la variable ch con el valor 'hola'
    ch = modificar_variable(ch) # Modifica la variable ch
    mostrar_variable(ch)  # Muestra la variable ch
    mostrar_final()

if __name__ == "__main__":
    main()