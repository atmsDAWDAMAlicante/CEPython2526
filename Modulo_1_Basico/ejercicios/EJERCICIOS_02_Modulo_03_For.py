# EJERCICIOS - 02 - Modulo - 03 - Bucle For

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Enunciado: Utilizando cinco bucles tipo for y en cada uno de ellos el tipo range() con tres argumentos,
# escribe el código Python necesario para que se muestre por pantalla la siguiente
# información tabulada con las siguientes cinco series aritméticas:
'''
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
20 23 26 29 32 35 38 41 44 47
10 14 18 22 26 30
40 35 30 25 20 15 10 5 0
'''

def ejercicio_01():
    print(f"---Ejercicio nº 1: Cinco bucles para cinco operaciones")
    mensaje_ej_1 = "" #Aquí se recogerá el string que se imprimirá por pantalla

    #1º Bucle: incremento +1
    for i in range(1,11,1):
        mensaje_ej_1 += f"{i:<3}"

    mensaje_ej_1 += "\n"

    #2º Bucle, incremento +2
    for i in range(2,21,2):
        mensaje_ej_1 += f"{i:<3}"

    mensaje_ej_1 += "\n"

    #3º Bucle, incremento +3 desde 20
    for i in range(20,48,3):
        mensaje_ej_1 += f"{i:<3}"

    mensaje_ej_1 += "\n"

    #4º Bucle: incremento +4 desde 10
    for i in range (10,31,4):
        mensaje_ej_1 += f"{i:<3}"

    mensaje_ej_1 += "\n"

    #5º Bucle: decremento -5 desde 40 hasta 0
    for i in range(40,-1,-5):
        mensaje_ej_1 += f"{i:<3}"


    #Salida final
    print(mensaje_ej_1)
    return mensaje_ej_1





#2. Enunciado: Crea un programa que muestre el mismo resultado que en el ejercicio anterior, pero
#utilizando ahora bucles tipo for con tipos range() de dos argumentos.


def ejercicio_02():
    print(f"---Ejercicio nº 2: Range con dos argumentos")
    mensaje_ej_2 = "" #Aquí se recogerá el string que se imprimirá por pantalla

    #1º Bucle: incremento +1
    for i in range(1,11):
        mensaje_ej_2 += f"{i:<3}"

    mensaje_ej_2 += "\n"

    #2º Bucle, incremento +2
    for i in range(2,21):
        if (i%2 == 0):
            mensaje_ej_2 += f"{i:<3}"
        

    mensaje_ej_2 += "\n"

    #3º Bucle, incremento +3 desde 20
    j = 17  # La variable j comprobará que i contiene un incremento de +3 dentro del bucle
    # Por eso j debe comenzar por i -3
    for i in range(20,48):
        if (i - 3) == j:
            mensaje_ej_2 += f"{i:<3}"
            j = i # Se actualiza j para la siguiente vuelta del bucle
    
    mensaje_ej_2 += "\n"

    #4º Bucle: incremento +4 desde 10
    j = 6 # La idea es la misma que la del bucle anterior
    # Aquí j debe comenzar por i - 4
    for i in range (10,31):
        if (i - 4) == j:
            mensaje_ej_2 += f"{i:<3}"
            j = i # se actualiza j para la siguiente vuelta del bucle

    mensaje_ej_2 += "\n"

    #5º Bucle: decremento -5 desde 40 hasta 0
    #HAY QUE USAR REVERSED
    for i in reversed(range(0,41)):
        if(i%5==0):
            mensaje_ej_2 += f"{i:<3}"
    
    #Salida final
    print(mensaje_ej_2)
    return mensaje_ej_2

#3. Enunciado: Crea un programa que muestre la tabla del ejercicio número 1, utilizando bucles tipo for
#con tipos range() que tengan solamente un argumento.
print(f"---Ejercicio nº 3: Dxxx")


def ejercicio_03():
    pass


#4. Enunciado: Escribe el código necesario para generar las siguientes siete secuencias de números
#utilizando bucles for.
'''
1 4 9 16 25 36 49 64 81 100
2 5 10 17 26 37 50 65 82 101
8 27 64 125 216 343
2 6 12 20 30 42 56
1 10 100 1000 10000
1.0 0.1 0.01 0.001 0.0001
1 -1 1 -1 1 -1 1 -1
'''
print(f"---Ejercicio nº 4: Dxxx")






#5. Enunciado: Haz que se pidan dos números enteros, siendo el segundo mayor o igual al primero.
#Muestra por pantalla todos los números enteros comprendidos entre los números
#introducidos, indicando en cada caso si el número es par o impar.
'''
Escribe un número entero: 6
Escribe un número entero mayor o igual que 6: 2
¡Te he pedido un número entero mayor que 6!

Escribe un número entero: 4
Escribe un número entero mayor o igual que 4: 8
El número 4 es par
El número 5 es impar
El número 6 es par
El número 7 es impar
El número 8 es par

Escribe un número entero: 5
Escribe un número entero mayor o igual que 5: 5
El número 5 es impar
'''


print(f"---Ejercicio nº 5: Dxxx")






#6. Enunciado: Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual
#que el primero. A continuación, el programa debe mostrar como resultado la suma de
#todos los enteros comprendidos entre el primero y el segundo incluidos ambos. Observa
#el formato del resultado en el modelo:

'''
Escribe un número entero: 7
Escribe un número entero mayor que 7: 7
¡Te he pedido un número entero mayor que 7!

Escribe un número entero: 30
Escribe un número entero mayor que 30: 32
La suma desde 30 hasta 32 es 93
30 + 31 + 32 = 93
'''
print(f"---Ejercicio nº 6: Dxxx")






#7. Enunciado: Escribe un programa que pida por pantalla un número entero y que a continuación calcule
#su factorial. En número ha de ser mayor que cero.

#El factorial de un entero n (n!) es el producto de los enteros desde el 1 hasta dicho número n.

'''
Escribe un número entero mayor que cero: -5
¡Le he pedido un número entero mayor que cero!
El factorial de un entero n (n!) es el producto de los enteros desde el 1 hasta dicho número n.

Escribe un número entero mayor que cero: 5
El factorial de 5 es: 120
'''
print(f"---Ejercicio nº 7: Dxxx")






#8. Enunciado: Escribe un programa que permita sumar números, la aplicación debe funcionar de la siguiente forma:
    #a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir
    #b. A continuación, el programa debe pedir cada uno de esos valores (pueden ser decimales).
    #c. Por último el programa calculará el número mayor, el menor, la suma y la media de
        #todos ellos y mostrará el resultado porpantalla. Ten en cuenta que sólo
        #mostraremos 2 decimales.
'''
¿Cuántos valores vas a introducir? -1
¡Imposible!

¿Cuántos valores vas a introducir? 5
Escribe el número 1: 25
Escribe el número 2: 30
Escribe el número 3: 10.5
Escribe el número 4: 14
Escribe el número 5: 23
Número mayor: 30.00 Número Menor: 10.50
La suma de los números que has escrito es 102.50
La media de los números que has escrito es 20.50
'''
print(f"---Ejercicio nº 8: Dxxx")







#9. Enunciado: Diseña un programa que detecte números negativos, la aplicación debe funcionar de la siguiente forma:
    #a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir.
    #b. A continuación, el programa ha de pedir cada uno de esos valores (pueden ser decimales)
    #c. Por último, el programa indicará cuántos de esos números son negativos

'''
¿Cuántos valores vas a introducir? -1
¡Imposible!

¿Cuántos valores vas a introducir?2
Escribe el número 1: 56

Escribe el número 2: -22
Has escrito 1 número negativo.

¿Cuántos valores vas a introducir?5
Escribe el número 1: 56
Escribe el número 2: -22
Escribe el número 3: 98
Escribe el número 4: -30
Escribe el número 5: -30
Has escrito 3 números negativos.
'''
print(f"---Ejercicio nº 9: Dxxx")



#10. Enunciado: Crea un programa que pida un valor entero mayor que cero y calcule todos sus divisores,
#mostrando el resultado con el formato indicado en el siguiente ejemplo (necesitarás
#utilizar una variable tipo lista).
'''
Escribe un número entero mayor que cero: -5
¡El número introducido debe ser un entero mayor de cero!
Escribe un número entero mayor que cero: 200
Los 12 divisores de 200 son 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 y 200.
'''
print(f"---Ejercicio nº 10: Dxxx")


#11. Enunciado: Tomando como punto de partida el programa anterior, escribe el código necesario para
#que el programa determine si el número es primo o no, el resultado podría ser:
'''
Escribe un número entero mayor que cero: -5
¡El número introducido debe ser un entero mayor de cero!

Escribe un número entero mayor que cero: 200
200 no es un número primo.
Los 12 divisores de 200 son 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 y 200.

Escribe un número entero mayor que cero: 7
7 es un número primo.
'''
print(f"---Ejercicio nº 11: Dxxx")



#12. ENTREGABLE - Enunciado: Escribe un programa que permita al usuario introducir un número entero positivo n.
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
'''
Introduce un número entero positivo: 28
Divisores propios: [1, 2, 4, 7, 14]
Suma de divisores: 28
El número 28 es PERFECTO.

Introduce un número entero positivo: 12
Divisores propios: [1, 2, 3, 4, 6]
Suma de divisores: 16
El número 12 es ABUNDANTE.

Introduce un número entero positivo: 220
Divisores propios: [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
Suma de divisores: 284
El número 220 es AMIGO del número 284.
'''

print(f"---Ejercicio nº 12: Dxxx")





#EJECUCIÓN
ejercicio_01()
ejercicio_02()
ejercicio_03()



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")