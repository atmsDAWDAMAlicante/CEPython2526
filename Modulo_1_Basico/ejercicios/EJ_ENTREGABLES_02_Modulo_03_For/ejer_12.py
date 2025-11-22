#EJERCICIOS ENTREGABLES UD 02 - Modulo 03 - For
#Ejercicio nº 12
#ALUMNO: ANGEL TOMÁS MORENO SENÉN

#Enunciado: Escribe un programa que permita al usuario introducir un número entero positivo n.
#El programa deberá:
    #a) Calcular todos los divisores propios del número (los que son menores que él mismo).
    #b) Calcular la suma de esos divisores.
    #c) Según el resultado, indicar:
        #− Si el número es perfecto (la suma de sus divisores propios es igual al número).
        #− Si es deficiente (la suma es menor que el número).
        #− Si es abundante (la suma es mayor que el número).
    #d) Para medalla de honor:
    #Comprobar si el número forma parte de una pareja de números amigos.
    #Es decir, si existe otro número m tal que la suma de los divisores propios de n es m y la
    #suma de los divisores propios de m es n 

import os
# para limpiar la terminal
os.system('cls')

# 1. Variables globales
tipo_numero = ("PERFECTO", "DEFICIENTE", "ABUNDANTE", "AMIGO") #Tupla con los nombres de los tipos de números

# 2.Función principal que pide un número, verifica que sea entero y llama a las funciones
def ejercicio_12():

    # Se pide el número
    while True:
        try:
            num = int(input("Introduce un número entero: "))
            identificar_divisores_y_suma(num)
            break # Interrumpe el bucle y no pide más números
        except ValueError:
            print("Lo siento. Introduce un número entero (esta vez acierta).")

#3. Función con los cálculos: PRIMERA PARTE: el bucle que identifica los divisores, 
# los introduce en la lista y los suma
def identificar_divisores_y_suma(num):
    # Aquí inicio las variables en lugar de hacerlas globales y luego las paso por parámetro
    mensaje_ej_12 = "" #Aquí se recogerá el string que se imprimirá por pantalla 
    suma_divisores = 0 # int encargado de sumar los divisores
    lista_de_divisores = [] #Esta lista recoge individualmente los divisores
    
    for i in range(1, num+1): #Bucle desde 1 (para evitar la división por 0) hasta el número pasado +1
        if (num%i == 0) and (i < num): # Evalúa que no haya resto Y que el contador sea menor al número pasado
            suma_divisores += i # Se suma i que es el divisor que cumple la condición
            lista_de_divisores.append(i) # y se añade a la lista de divisores

    #Aquí se genera la primera parte del fstring que se mostrará como resultado
    mensaje_ej_12 = f"Divisores propios: {lista_de_divisores}\nSuma de divisores: {suma_divisores}"
    el_tipo_de_numero(num, suma_divisores, mensaje_ej_12) # se pasan las variables por parámetro

#3. Siguen los cálculos: SEGUNDA PARTE: El tipo de número 
def el_tipo_de_numero(num, suma_divisores, mensaje_ej_12):
    if (num == suma_divisores):# Si el número es perfecto
        mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[0]}."

    # Para identificar sólo si es deficiente o abundante, basta con anidar un elif num > suma_divisores = deficiente y else = abundante

    else: #Para saber si es amigo hay que añadir un else y dentro introducir otro condicional if
        # Primero un bucle para obtener la suma de los divisores del número que es la suma de los divisores del número original
        # defino una variable que contendrá la suma de divisores del numero divisor: suma_divisores_del_divisor
        suma_divisores_del_divisor = 0
        # Copio el anterior bucle y cambio la i por j y el número introducido por la suma de divisores de este (calculado antes)
        for j in range(1, suma_divisores+1): #Bucle desde 1 (para evitar la división por 0) hasta el número pasado +1
            if (suma_divisores%j == 0) and (j < suma_divisores): # Evalúa que no haya resto Y que el contador sea menor al número pasado
                suma_divisores_del_divisor += j # Se suma j que es el divisor que cumple la condición

        # Ahora se puede evaluar si el número es amigo y, en caso contrario ver si es deficiente o abundante.
        # El if evalúa primero si el número es amigo
        if (num == suma_divisores_del_divisor):
            mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[3]} del número {suma_divisores}."
        # En caso contrario... se introduce un nuevo condicional que, ahora sí discrimina 
        # si es deficiente o abundante
        else:
            if (num > suma_divisores):
                mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[1]}."
            else:
                mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[2]}."
    
    # IMPRESIÓN DEL RESULTADO FINAL
    print(mensaje_ej_12)

#Inicio del programa
print(f"---Ejercicio nº 12: Entregable: numeros Perfectos, Deficientes, Abundantes o Amigos")
ejercicio_12()
