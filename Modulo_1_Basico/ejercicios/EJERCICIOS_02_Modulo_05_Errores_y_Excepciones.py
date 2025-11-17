# EJERCICIOS - 02 - Modulo - 05 - Errores y Excepciones

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Enunciado: Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
# programa se bloquee y que explique al usuario la causa y/o solución:
'''
resultado = 10/0

No es posible dividir entre cero, debes introducir un número distinto.
'''

def ejercicio_01(num1, num2):
    print(f"---Ejercicio nº 1: División por cero")
    try:
        return int(num1)/int(num2)
    except ZeroDivisionError:
        return "No es posible dividir entre cero, debes introducir un número distinto."





#2. Enunciado: Partimos de la siguiente lista:
'''
lista=['gato', 'perro', 'ratón', 'pato', 'elefante']
'''
# Crea un programa que solicite el índice de un elemento de la lista y que a continuación
# muestre dicho elemento por pantalla.
'''
['gato', 'perro', 'ratón', 'pato', 'elefante']
Introduce el índice del elemento de la lista que quieres mostrar por pantalla:3
pato
'''
# En caso de que el índice sea un número entero demasiado mayor (>4) se producirá un error.
# Crea una excepción para evitar que el programa se bloquee y que explique al usuario la causa
# y solución.


def ejercicio_02(animal):
    print(f"---Ejercicio nº 2: Lista de animales")
    lista=['gato', 'perro', 'ratón', 'pato', 'elefante']
    try:
        return lista[animal]
    except IndexError:
            return "El índice se encuentra fuera del rango.\nDebes utilizar un número mayor o igual que cero y menor que la longitud de la lista."
print(ejercicio_02(3)) #pato
print(ejercicio_02(6)) # Error



#3. ENTREGABLE - Enunciado: Partimos del siguiente diccionario:
'''
colores = { 'rojo':'red', 'verde':'green', 'azul':'blue', 'negro':'black'}
'''
# Crea un programa que solicite un término del diccionario para mostrar su valor asociado por
# pantalla:
'''
Introduce el nombre de un color en español: azul
azul en inglés se dice blue
'''
#En caso de que el término no esté incluido en el diccionario se producirá un error. Crea una
#excepción para evitar que el programa se bloquee y que explique al usuario la causa y
#solución.

'''
Introduce el nombre de un color en español: amarillo
Error: El término amarillo no se encuentra en este diccionario, debes probar con
otro que sí exista.
'''

def ejercicio_03(color):
    print(f"---Ejercicio nº 3: Diccionario de colores")
    colores = {'rojo':'red', 'verde':'green', 'azul':'blue', 'negro':'black'}
    try:
        colores.get(color) # esto no hace nada
        return f'{color} en inglés se dice {colores[color]}'
    except KeyError:
        return f'Error: El término {color} no se encuentra en este diccionario, debes probar con otro que sí exista.'
print(ejercicio_03("azul"))
print(ejercicio_03("amarillo"))

#4. Enunciado: Crea un programa que solicite dos números enteros por pantalla y muestre el resultado de
# su suma. En caso de que uno de los valores introducidos sea una cadena de caracteres el
# programa debe gestionar el error informando de la causa y solución.
'''
Introduce el primer valor: 5
Introduce el segundo valor: 4
5 + 4 = 9


Introduce el primer valor: 3
Introduce el segundo valor: 2.5
El valor introducido no es un número entero
'''


def ejercicio_04(num1, num2): #ESTO NECESITA UNA SEGUNDA LECTURA CON isinstance()
    print(f"---Ejercicio nº 4: Operaciones con enteros")
    try:
            #num1 = int(num1)
            #num2 = int(num2)
        if (type(num1)!=int):
            raise ValueError ("El valor introducido no es un número entero")
        elif (type(num2)!=int):
            raise ValueError("El valor introducido no es un número entero")
        else:
            return (f'{num1} + {num2} = {num1+num2}')
    except ValueError:
        return "El valor introducido no es un número entero"

print(ejercicio_04(5,4.5))

#5. ENTREGABLE - Enunciado: Partiremos de la siguiente lista:
'''
elementos = [1, ‘pie’, -2]
'''
# Realiza una función llamada agregar_una_vez(lista, elemento) que reciba como parámetros
# una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición
# de no repetir ningún elemento. Además, si este elemento ya se encuentra en la lista se debe
# invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
# Error: Imposible añadir elementos duplicados => [elemento].
# Cuando tengas la función crea un programa que permita añadir elementos a la lista de forma
# indefinida. Intenta añadir los siguientes valores a la lista: 10, “pie”, "Hola" y luego muestra su
#contenido.
# Sugerencia: Puedes utilizar la sintaxis "elemento in lista", si el elemento está en la lista genera
# un valor True, si no lo está genera un valor False

'''
La lista actual es: [1, 'pie', -2]
Valor que quieres añadir a la lista: 10
La lista actual es: [1, 'pie', -2, '10']
Valor que quieres añadir a la lista: pie
Error: Imposible añadir elementos duplicados => pie
La lista actual es: [1, 'pie', -2, '10']
Valor que quieres añadir a la lista: Hola
La lista actual es: [1, 'pie', -2, '10', 'Hola']
'''

def ejercicio_05(num):
    print(f"---Ejercicio nº 5: Dxxx")






#6. Enunciado: Escribe el código de una función que ha de ser capaz de aceptar números enteros positivos.
# La función ha de chequear que el número introducido cumple la condición dada. La función
# ha de ser capaz de gestionar los valores que no sean enteros o que sean enteros negativos
# o si se introduce un texto o si pulsamos “enter” sin haber introducido un valor, informando
# del error.


def ejercicio_06(num):
    print(f"---Ejercicio nº 6: Dxxx")






#7. Enunciado: Mejora el programa anterior consiguiendo que en caso de excepción la función solicite un
# nuevo valor hasta que este tenga el formato correcto.

'''
Introduce un número entero positivo: -5
El valor es número entero negativo
Introduce un número entero positivo: 5.2
El número es decimal
Introduce un número entero positivo: hola
El valor introducido no es un número
Introduce un número entero positivo: 4
4
'''

def ejercicio_07(num):
    print(f"---Ejercicio nº 7: Dxxx")






#8. ENTREGABLE - Enunciado: Crea un programa llamado “Gestor de inventario” que combine
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

def ejercicio_08(num):
    print(f"---Ejercicio nº 8: Dxxx")






#9. Enunciado: 


def ejercicio_09(num):
    print(f"---Ejercicio nº 9: Dxxx")



#10. Enunciado: 


def ejercicio_10(num):
    print(f"---Ejercicio nº 10: Dxxx")


#11. Enunciado: 


def ejercicio_11(num):
    print(f"---Ejercicio nº 11: Dxxx")



#12. Enunciado: 


def ejercicio_12(num):
    print(f"---Ejercicio nº 12: Dxxx")





#13. Enunciado: 


def ejercicio_13(num):
    print(f"---Ejercicio nº 13: Dxxx")



#14. ENTREGABLE - Enunciado: 


def ejercicio_14(num):
    print(f"---Ejercicio nº 14: Dxxx")



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")