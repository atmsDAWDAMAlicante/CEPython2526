#EJERCICIOS ENTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 5
# ALUMNO: XX

#Enunciado: Partiremos de la siguiente lista:

    #elementos = [1, ‘pie’, -2]

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

import os
# para limpiar la terminal
os.system('cls')

#1. Variables globales
elementos = [1, 'pie', -2]

# 2. Funciones

# 2.1 Función principal del programa

def ejercicio_05(): #Primera función: pide el elemento.

    # Se repite indefinidamente
    while True:
        elemento = input(f"Introduce un elemento no repetido:\n>>>>>  ") # Pide el elemento
        #resultado = f"La lista actual es: {elementos}\nValor que quieres añadir a la lista: {elemento}"
        resultado = "" # Se actualiza la cadena resultado a ""
        try: # Primero intenta converitr el elemento a un entero
            elemento = int(elemento) # Primero se intenta convertir el número a entero
            # Si lo consigue lo envía la funcion agregar_una_vez como ENTERO para añadirlo
            resultado = agregar_una_vez(elemento)
        except ValueError: # Si se lanza el error, lo envía como STRING
            resultado = agregar_una_vez(elemento)
        # Las dos llamadas esperan de retorno el string que se imprime en pantalla
        finally: # Siempre se imprime el resultado, sea el que sea
            print(resultado)

# 2.2 Función que añade el elemento si no está y devuelve un fstring con el resultado

def agregar_una_vez(elemento): # Recibimos el elemento ya como entero o como string
    try: # Primero intenta ver si está en la lista (como entero o como string)
        if (elemento in elementos): # Si el elemento está en la lista lanza la excepción
            raise Exception
        else:
            # No está en la lista
            elementos.append(elemento) # Lo añade a la lista
            print(f"\nHas añadido {elemento}.") # Imprime que lo ha añadido
            resultado = f"\nLa lista actual es: {elementos}" # Se actualiza el fstring
        return resultado # retorna el  fstring para imprimirlo en el finally de la función principal
    
    except Exception: # Se actualiza el fstring con el error
        resultado = f"\nError: Imposible añadir elementos duplicados => {elemento}\nLa lista actual es: {elementos}"
        return resultado # retorna el  fstring para imprimirlo en el finally de la función principal


#Inicio del programa
print(f"---Ejercicio nº 5: Agregar elemento no repetido")
ejercicio_05()


