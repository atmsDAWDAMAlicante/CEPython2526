#EJERCICIOS NTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 8
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

#Enunciado: Enunciado: Crea un programa llamado “Gestor de inventario” que combine
# todos los conceptos de gestión de errores vistos en clase.

#El programa gestiona un inventario de productos, guardados en un diccionario, donde:
    #− la clave es el nombre del producto,
    #− el valor es la cantidad disponible (entero positivo).

#El usuario podrá realizar las siguientes operaciones mediante un menú:
    #1. Añadir producto
    #2. Consultar cantidad
    #3. Modificar cantidad
    #4. Eliminar producto
    #5. Mostrar inventario completo
    #6. Salir del programa

#1. El programa debe manejar correctamente todos los posibles errores:
    #− Si el usuario introduce una opción no válida entonces mostrar mensaje de error.
    #− Si se intenta consultar o eliminar un producto que no existe, capturar KeyError.
    #− Si la cantidad introducida no es un número entero positivo, capturar ValueError.
    #− Si se introduce un texto vacío o se pulsa Enter hay que mostrar advertencia.
    #− Si el usuario intenta introducir un valor no numérico en una operación numérica
    #tenemos que controlarlo con try/except.
    #− Debe usarse try, except, else y finally al menos una vez en el código.

'''
GESTOR DE INVENTARIO
1. Añadir producto
2. Consultar cantidad
3. Modificar cantidad
4. Eliminar producto
5. Mostrar inventario completo
6. Salir

Selecciona una opción (1-6): 1
Introduce el nombre del producto: ratón
Introduce la cantidad: -5
Error: Debe ser un número positivo.
Introduce un número válido.

Introduce la cantidad: diez
Error: invalid literal for int() with base 10: 'diez'
Introduce un número válido.

Introduce el nombre del producto: ratón
Introduce la cantidad: 10
Producto 'ratón' añadido correctamente.
Operación finalizada.

Selecciona una opción (1-6): 2
Producto que consultar: monitor
Error: 'monitor'
Solución: Asegúrate de que el producto existe en el inventario.
Operación finalizada.
'''

import os


os.system('cls')

# Formación del menú principal del programa:
menu_lista= ["GESTOR DE INVENTARIO", "1. Añadir producto", "2. Consultar cantidad", 
            "3. Modificar cantidad", "4. Eliminar producto", "5. Mostrar inventario completo", 
            "6. Salir"]
menu = ""
for elemento_menu in menu_lista:
    menu += f'{elemento_menu}\n'

# Formación del stock al iniciarse el programa
productos = {"teclado": 4, "ratón": 5, "impresora": 1, "pendrive": 10, "monitor": 3}
linea = "-----------------------------"

# 1ª Función: la función principal
def main():
    while True:
        print(f'{linea}{menu}{linea}')
        opcion_del_usuario = validar_opcion(input("Seleccione su opción: "))

        if opcion_del_usuario == 6:
            print(f"Usted ha seleccionado: {menu_lista[6]}\nAdiós. Vuelva pronto.")
            break
        else:
            operaciones(opcion_del_usuario)

# 2º Función: encargada de validar que se selecciona una de las opciones del menú
class NumeroFueraRango(Exception):
    pass


def validar_opcion(num):
    while True:
        try:
            opcion = int(num)
            if opcion < 1 or opcion > 6:
                raise NumeroFueraRango
            return opcion
        except ValueError:
            print("Error: Debes introducir un número entero.")
        except NumeroFueraRango:
            print("Error: Introduce un número del 1 al 6.")
        
        # si llegamos aquí significa que hubo un error, pedimos de nuevo
        num = input("Seleccione su opción: ")



def operaciones(num):
    print(f'Vd. ha seleccionado: {menu_lista[num]}')
    print(f'{linea}\n¿Otra operación?\n{linea}')


# Comienzo del programa
print(f"---Ejercicio nº 8: Gestor de inventario")
main()
    

    
    


