# ENUNCIADO Ejercicio 4: 
# Escribir un programa que pregunte al usuario su peso en kg y lo
# almacene en una variable, El programa debe mostrar al final el peso
# introducido por el usuario.

import os
os.system("cls")
num_programa = 4
inicio = f'=== INICIO DEL EJERCICIO nº {num_programa} ===\n'
fin = f'\n=== FIN DEL PROGRAMA ==='

# Modelo 
def validar_peso(peso):
    try:
        peso = float(peso)
        return peso
    except ValueError:
        #print("Error: Introduce tu peso con un número válido.")
        # EL MODELO NO PUEDE TENER UN PRINT
        return None
    
# Vista
def mostrar_inicio():
    print(inicio)

def obtener_peso():
    peso = input("Introduce tu peso en kg: ")
    return peso

def mostrar_peso(peso):
    print(f"Tu peso es: {peso} kg{fin}")

def mostrar_error(): # IMPORTANTE: la vista NO vuelve a pedir el dato
    print("Error: Introduce tu peso con un número válido.")


# Controlador
def main():
    mostrar_inicio() # OJO - Sólo la vista lleva los prints
    while True:
        peso_a_pedir = obtener_peso()
        peso = validar_peso(peso_a_pedir)
        if peso is not None:
            mostrar_peso(peso)
            break
        else: # En caso de error, se llama a la vista para mostrar el error
            mostrar_error() # No se añade nada más, el bucle se repite, no lleva 
            # ni break ni main() ni nada por el estilo, se repite el bucle
 

if __name__ == "__main__":
    main()