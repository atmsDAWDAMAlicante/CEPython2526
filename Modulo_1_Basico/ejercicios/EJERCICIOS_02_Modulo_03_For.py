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


# En este caso la cuestión está en que el condicional evalúe el punto de partida
def ejercicio_03():
    print(f"---Ejercicio nº 3: Range con un argumento")
    mensaje_ej_3 = "" #Aquí se recogerá el string que se imprimirá por pantalla

    #1º Bucle: incremento +1
    for i in range(11):
        if (i > 0):
            mensaje_ej_3 += f"{i:<3}"

    mensaje_ej_3 += "\n"

    #2º Bucle, incremento +2
    for i in range(21):
        if (i > 0) and (i%2 == 0):
            mensaje_ej_3 += f"{i:<3}"
        
    mensaje_ej_3 += "\n"

    #3º Bucle, incremento +3 desde 20
    j = 17  # La variable j comprobará que i contiene un incremento de +3 dentro del bucle
    # Por eso j debe comenzar por i -3
    for i in range(20,48):
        if (i > 19) and ((i - 3) == j):
            mensaje_ej_3 += f"{i:<3}"
            j = i # Se actualiza j para la siguiente vuelta del bucle
    
    mensaje_ej_3 += "\n"

    #4º Bucle: incremento +4 desde 10
    j = 6 # La idea es la misma que la del bucle anterior
    # Aquí j debe comenzar por i - 4
    for i in range (31):
        if (i > 9) and ((i - 4) == j):
            mensaje_ej_3 += f"{i:<3}"
            j = i # se actualiza j para la siguiente vuelta del bucle

    mensaje_ej_3 += "\n"

    #5º Bucle: decremento -5 desde 40 hasta 0
    #HAY QUE USAR REVERSED
    for i in reversed(range(41)): #Atención al parámetro de reversed(range(n))
        if (i < 41) and (i%5==0):
            mensaje_ej_3 += f"{i:<3}"
    
    #Salida final
    print(mensaje_ej_3)
    return mensaje_ej_3


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
def ejercicio_04():
    print(f"---Ejercicio nº 4: Bucles variados")

    mensaje_ej_4 = "" #Aquí se recogerá el string que se imprimirá por pantalla

    #1º Bucle: 1 4 9 16 25 36 49 64 81 100
    # Explicación del bucle: cada vuelta se le suma un número que se incrementa +2
    # 1 + x = 4 por tanto x = 3
    # 4 + x = 9 por tanto X = 5
    # 9 + x = 16 por tanto x = 7
    numero_base = 1 # esta variable se incrementa a cada vuelta y se añade al string
    numero_incremento = 3 # esta variable es la que se incrementa cada vuelta en 2 para sumarla a la base
    espacio_plus = "" # esta cadena posibilitará que se muestre el espacio añadido al fstring sin modificar el 3 de formato
    for i in range(10): 
        if (numero_base >= 100):
            espacio_plus = ""
        mensaje_ej_4 += f"{espacio_plus}{numero_base:<3}"
        numero_base += numero_incremento
        numero_incremento += 2

    print(mensaje_ej_4)
    print("--------------")
    mensaje_ej_4 += "\n"


    #2º Bucle: 2 5 10 17 26 37 50 65 82 101
    # El número base se incrementa cada vuelta con el número impar siguiente al que se le suma 2
    numero_base = 2 # variable que se inrementa a cada vuelta con un número impar + 2
    numero_incremento = 3 # cada vuelta se incrementará + 2
    espacio_plus = "" #para mostrar el espacio en el número mayor que 100

    for i in range(10):
        if (numero_base > 100):
            espacio_plus = ""
        mensaje_ej_4 += f"{espacio_plus}{numero_base:<3}"
        numero_base += numero_incremento
        numero_incremento += 2

    print(mensaje_ej_4)
    print("--------------")
    mensaje_ej_4 += "\n"


    #3º Bucle:8 27 64 125 216 343
    # Números elevados a la tercera potencia 
    import math #para utilizar Pow
    resultado = 0

    for i in range(2,8):
        resultado = pow(i,3)

        if (resultado >= 100): # Condicional que cambia los espacios del fstring en función del resultado de la potencia
            mensaje_ej_4 += f"{resultado:<4}"
        else: 
            mensaje_ej_4 += f"{resultado:<3}"

    print(mensaje_ej_4)
    print("--------------")
    mensaje_ej_4 += "\n"

    #4º Bucle: 2 6 12 20 30 42 56
    #2*1 = 2
    #2*(1+2)= 6
    #2*(1+2+3) = 12
    #2*(1+2+3+4) = 20
    #2*(1+2+3+4+5) = 30
    #2*(1+2+3+4+5+6) = 42
    #2*(1+2+3+4+5+6+7) = 56

    for i in range(1,8):
        multiplicador = 0 # Esta variable contador recogerá las sumas para multiplicarlas por 2
        for j in range(1,i+1): # Segundo bucle anidado: genera el multiplicador con las sumas 1+2+3+ etc
            multiplicador += j
        mensaje_ej_4 += f"{2 * multiplicador:<3}"
    
    print(mensaje_ej_4)
    print("--------------")
    mensaje_ej_4 += "\n"

    #5º Bucle: 1 10 100 1000 10000
    pass

    mensaje_ej_4 += "\n"
    #6º Bucle: 1.0 0.1 0.01 0.001 0.0001
    pass

    mensaje_ej_4 += "\n"
    #7º Bucle: 1 -1 1 -1 1 -1 1 -1
    pass

    
    #Salida final
    print(mensaje_ej_4)
    return mensaje_ej_4


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

def parImpar(num): # Monto una función para saber si es par/impar, que me hará falta seguro
    if (num%2==0):
        return True
    else:
        return False

def ejercicio_05(num1, num2):
    print(f"---Ejercicio nº 5: Pares e impares")

    mensaje_ej_5 = "" #Aquí se recogerá el string que se imprimirá por pantalla

    #para el supuesto que los números entraran a traǘes de un input()
    num1 = int(num1)
    num2 = int(num2)
    cadenaPar = ""

    if (num1 > num2): #Mensaje si el segundo número es menor que el primero
        mensaje_ej_5 =  f"¡Te he pedido un número entero mayor que {num1}!"

    elif (num1 == num2): #Supuesto para el caso que los números sean iguales
        esPar = parImpar(num1)
        if (esPar):
            mensaje_ej_5 = f"El número {num1} es par"
        else:
            mensaje_ej_5 = f"El número {num1} es impar"

    else: # El resto de casos se forma el fstring dentro de un bucle
        for i in range(num1,num2+1):
            esPar = parImpar(i)
            if (esPar):
                mensaje_ej_5 += f"El número {i} es par\n"
            else:
                mensaje_ej_5 += f"El número {i} es impar\n"

    #Igual debería haber montado los strings en otra función

    #Salida final
    print(mensaje_ej_5)
    return mensaje_ej_5


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
def ejercicio_06(num1, num2):
    print(f"---Ejercicio nº 6: Sumatorio")

    #para el supuesto que los números entraran a traǘes de un input()
    num1 = int(num1)
    num2 = int(num2)
    cadenaPar = ""

    if (num1 > num2): #Mensaje si el segundo número es menor que el primero
        mensaje_ej_5 =  f"¡Te he pedido un número entero mayor que {num1}!"
    else:
        pass


    mensaje_ej_6 = "" #Aquí se recogerá el string que se imprimirá por pantalla


    
    #Salida final
    print(mensaje_ej_6)
    return mensaje_ej_6

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
def ejercicio_07(num):
    print(f"---Ejercicio nº 7: Factorial")
    pass






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

def ejercicio_08(i):
    print(f"---Ejercicio nº 8: xxx")
'''   
    j = i + 4
    return prueba_08(j)

def prueba_08(j):
    k = 1 + j
    return k

'''


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

def ejercicio_09():
    print(f"---Ejercicio nº 9: xxx")
    pass



#10. Enunciado: Crea un programa que pida un valor entero mayor que cero y calcule todos sus divisores,
#mostrando el resultado con el formato indicado en el siguiente ejemplo (necesitarás
#utilizar una variable tipo lista).
'''
Escribe un número entero mayor que cero: -5
¡El número introducido debe ser un entero mayor de cero!
Escribe un número entero mayor que cero: 200
Los 12 divisores de 200 son 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 y 200.
'''

def ejercicio_10(num):
    print(f"---Ejercicio nº 10: Divisores")
    pass


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
def ejercicio_11():
    print(f"---Ejercicio nº 11: Numeros primos y divisores")
    pass



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

def ejercicio_12(num):
    print(f"---Ejercicio nº 12: Entregable:")
    pass





#EJECUCIÓN
ejercicio_01()
ejercicio_02()
ejercicio_03()
ejercicio_04()
ejercicio_05(6,2)
ejercicio_05(4,8)
ejercicio_05(5,5)
#ejercicio_06()
ejercicio_07()
#ejercicio_08()
ejercicio_09()
ejercicio_10()
ejercicio_11()
ejercicio_12()



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")