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

# 1ª Función: la función principal



# 2º Función: encargada de validar que se selecciona una de las opciones del menú
def validar_opcion():
    opcion = 0
    opcion_correcta = False
    while (opcion_correcta != True): # Bucle que mantiene la petición de un entero del 1 al 6
        try:
            opcion = int(input("Seleccione su opción: "))
            if (opcion > 6) or (opcion < 1):
                raise ValueError
            opcion_correcta = True
        except ValueError:
            print("Opcion del menú no permitida\nIntroduzca un número del 1 al 6")
    return opcion 

def operaciones(num):
    if (num == 1):
        print(num)
    elif (num == 2):
        print(num)
    elif (num == 3):
        print(num)
    elif (num == 4):
        print (num)
    else:
        print(num)


# Comienzo del programa
print(f"---Ejercicio nº 8: Gestor de inventario")
print(menu)
opcion = validar_opcion()
print(f'Vd. ha seleccionado: {menu_lista[opcion]}')
while (opcion != 6):
    operaciones(opcion)
    opcion = validar_opcion()
else:
    print("Encantados de servirle. Vuelva pronto.")

    
    


