# ENUNCIADO Ejercicio 18: Ordenar una lista de tuplas
# Escribir un programa que permita ordenar una lista de tuplas L 
# en orden ascendente, basándose en el segundo elemento de la tupla.
# La lista que consideraremos en este ejercicio es:
# L = [("Manzana", 15),("Banana", 8), ("Fresa',' 12), ("Kiwi", 9), ("Melocotón',' 2)]
# 
# La lista L que debemos tener al final del programa (después del ordenamiento):
# L = [("Melocotón",2), ("Banana" ,8), ("Kiwi" ,9), ("Fresa" ,12), ("Manzana" ,15)]

import os, modulo as md
os.system("cls")
num_programa = 18

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