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

# 1. BLOQUE DE VARIABLES GLOBALES

# 1.1 - Formación del menú principal del programa:
menu_lista= ["GESTOR DE INVENTARIO", "1. Añadir producto", "2. Consultar cantidad", 
            "3. Modificar cantidad", "4. Eliminar producto", "5. Mostrar inventario completo", 
            "6. Salir"]
menu = ""
for elemento_menu in menu_lista:
    menu += f'{elemento_menu}\n'

# 1.2 - Formación del stock al iniciarse el programa
productos = {"teclado": 4, "ratón": 5, "impresora": 1, "pendrive": 10, "monitor": 3}
linea = "-----------------------------"

# 2. BLOQUE DE LAS FUNCIONES DEL MENÚ PRINCIPAL

# 2.1ª Función: la función principal
def main():
    while True: # Bucle que se repite para que el usuario elija qué hacer tras cada operación
        print(f'{linea}\n{menu}{linea}') # Imprime las 6 opciones; el fstring se forma fuera
        # Llamada a la función que valida la opción del usuario
        opcion_del_usuario = validar_opcion(input("Seleccione su opción: "))
        # Sólo retorna un valor válido entre 1 y 6
        # Si es 6, se termina el programa
        if opcion_del_usuario == 6:
            print(f"Usted ha seleccionado: {menu_lista[6]}\nAdiós. Vuelva pronto.")
            break
        else: # Si es una opción de 1 a 5 se envía ese entero a la función operaciones()
            operaciones(opcion_del_usuario)

# 2.2º Función: encargada de validar que se selecciona una de las opciones del menú

# Antes, se crea una clase de excepcion. Lo que está en paréntesis es que hereda de Exception
class ExcepcionPersonalizada(Exception): #esto es complicado
    pass


def validar_opcion(num):
    while True: # Aquí se vuelve a repetir un bucle hasta que el usuario introduce un numero válido
        try:
            opcion = int(num) # Intenta convertirlo a entero
            if ((opcion < 1) or (opcion > 6)): # Si es un entero pero no está entre 1 y 6
                raise ExcepcionPersonalizada # Lanza la excepción personalizada
            return opcion # Si es un número de 1 al 6, lo devuelve (el 6 sale del programa)
        # Si han habido problemas saltan las excepciones
        except ValueError: # si no se ha introducido un número entero
            print(">>>Debes introducir un número entero.")
        except ExcepcionPersonalizada: # si el número no está entre 1 y 6
            print(">>>Introduce un número del 1 al 6.")
        
        # Este input se repite con el bucle hasta que se introduce un número del 1 al 6
        # porque, si es del 1 al 6 se sale con el return
        num = input("Seleccione su opción: ") # Con esto se arregla el menú principal
        

# 3. BLOQUE DE FUNCIONES DE LAS OPERACIONES 

# 3.1 - Funcion que distribuye la operación pasada por parámetro
# Nota: la 5, inventario, no llama a ninguna función.
def operaciones(num):
    print(f'Vd. ha seleccionado: {menu_lista[num]}') # Un print con información
    if (num == 1): # Añadir producto
        añadir_producto()
    elif (num == 2): # Consultar cantidad
        consultar_cantidad()
    elif (num == 3): # Modificar cantidad
        modificar_cantidad()
    elif (num == 4): # Eliminar producto
        eliminar_producto()
    else: # Mostrar el inventario
    # Aquí no hace falta hacer nada excepcional
        print(f'{linea}\nINVENTARIO COMPLETO:')
        for elemento, cantidad in productos.items():
            print(f'- {elemento} - Cantidad: {cantidad}')
        print(f'---Total de productos: {len(productos)}')
    print(f'{linea}\n¿Otra operación?\n{linea}')

# 3.2 - Función: añadir producto (añadir elemento y su cantidad) - Parámetro: 1

def añadir_producto():
    elemento = pide_elemento()
    cantidad = pide_cantidad(input("Introduzca cuantos productos entran en el stock: "))
    try:
        productos[elemento]
    except KeyError:
        productos[elemento] = cantidad
        print(f'+++NUEVO INVENTARIO')
        operaciones(5)
    else:
        print(f'>>>No podemos atender su petición, "{elemento}" ya existe en el inventario.')

# 3.3 - Función: consultar cantidad - Parámetro: 2

def consultar_cantidad():
    pass

# 3.4 - Funcion: modificar cantidad - Parámetro: 3

def modificar_cantidad():
    pass

# 3.5 - Función: eliminar producto - Parámetro: 4

def eliminar_producto():
    '''
    Función que elimina un producto del inventario que se le pasa por parámetro.
    '''
    elemento = pide_elemento()
    try:
        productos.pop(elemento)
        print(f'---NUEVO INVENTARIO')
        operaciones(5)
    except KeyError:
        print(f'>>>No podemos atender su petición ya que "{elemento}" no existe en el inventario.')


# 4. BLOQUE DE FUNCIONES QUE VALIDAN LO QUE INTRODUCE EL USUARIO (en operaciones)

# 4.1 - Funcion que comprueba que no se introduce un elemento vacío
def pide_elemento():
    while True:
        try:
            elemento = input("Introduzca el nombre del producto: ").strip()
            if elemento == "":
                raise ValueError
            else:
                return elemento
        except ValueError:
            print(">>>El nombre del producto no puede estar vacío.")
        elemento = input("Introduzca el nombre del producto (esta vez, correctamente): ").strip()

# 4.2 - Funcion que comprueba que si el elemento existe
def comprobar_elemento(elemento):
    try:
        existe = productos[elemento]
        return existe
    except KeyError:
        print(f">>>'{elemento}' no existe en el inventario.")

# 4.3 - Funcion que comprueba que la cantidad introducida es un entero mayor que 0
def pide_cantidad(num):
    while True:
        try:
            cantidad = int(num)
            if (cantidad <= 0):
                raise ExcepcionPersonalizada
            return cantidad
        except ValueError: # si no se ha introducido un número entero
            print(">>>La cantidad debe ser un número entero.")
        except ExcepcionPersonalizada: # si el número no es positivo    
            print(">>>La cantiad debe ser un número positivo.")
        num = input("Reintroduzca la cantidad (esta vez, correctamente): ")


# Comienzo del programa
print(f"---Ejercicio nº 8: Gestor de inventario")
#help(eliminar_producto)
main()
    

    
    


