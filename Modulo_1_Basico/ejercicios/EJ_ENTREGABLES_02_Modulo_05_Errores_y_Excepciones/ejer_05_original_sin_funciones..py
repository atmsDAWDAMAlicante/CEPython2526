#EJERCICIOS ENTREGABLES UD 02 - Modulo 05 - Errores y excepciones
#Ejercicio nº 5
#ALUMNO: ANGEL TOMÁS MORENO SENÉN

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


def agregar_una_vez(lista, elemento): #El ejercicio 5
    #print(f"---Ejercicio nº 5: Agregar elemento no repetido")
    # Se recibe la lista y se forma la primera parte del fstring
    try:
        resultado = f"La lista actual es: {lista}\nValor que quieres añadir a la lista: {elemento}"
        # Se busca el duplicado
        # for i in lista: --> me puedo ahorrar el bucle con un in
        if (elemento in lista): # Si el elemento está en la lista
            raise Exception
        else:
            # No está en la lista
            lista.append(elemento) # Lo añade a la lista
            # Se actualiza el fstring
            resultado += f"\nLa lista actual es: {lista}"
        return resultado
    except Exception:
        resultado += f"\nError: Imposible añadir elementos duplicados => {elemento}\nLa lista actual es: {lista}"
        return resultado

print(agregar_una_vez([1, 'pie', -2], 10))
print(agregar_una_vez([1, 'pie', -2], 'pie'))

