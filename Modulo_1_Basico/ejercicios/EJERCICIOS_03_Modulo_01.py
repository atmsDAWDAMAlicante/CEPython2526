# EJERCICIOS - 03 - Modulo - 01 - Funciones I

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios del bloque Funciones 1\n{linea}")



#1. Enunciado: Escribe el siguiente código y añade los comentarios necesarios para explicar su funcionamiento.
print(f"---Ejercicio nº 1: Explicar código")
def subrutina():
    global a # hay que declarar global la variable para que se pueda modificar dentro de la función
    print(a)
    a += 10
    return

a = 33 # se asigna valor a la variable
subrutina() # se llama a la función (subir)
print(a)
#QueDevuelveElEjercicio1 = subrutina()
#print(QueDevuelveElEjercicio1)

print(linea)

#2. Enunciado: ¿Qué ocurre en el programa anterior si eliminamos la segunda línea de código (global a)?
#Añade al código los comentarios necesarios para explicar este cambio de funcionamiento.
print(f"---Ejercicio nº 2: Pues que no va")
print("Sin el global no se puede modificar la variable dentro de la función")

print(linea)


#3. Enunciado: Crea un nuevo módulo y escribe en él el siguiente código añadiendo los comentarios
#necesarios para explicar su funcionamiento.
print(f"---Ejercicio nº 3: Explicación de uso de variables globales")
def subrutina():
    global b
    # print(b) # El programa falla aquí porque la variable no ha sido definida aún
    b = 21
    return

subrutina() # llama a la función antes de asignar valor; se le asigna dentro como global
b = 20 # se modifica después de llamada a la función
print(b)

print(linea)


#4. Enunciado: Añade los comentarios necesarios para explicar el funcionamiento del código:
print(f"---Ejercicio nº 4: Explicación del uso de variables globales")
def funcion():
    global c
    c = 10
    print(c)
    return
c = 33
funcion()
print(c)
# Esto imprimirá 10-10
print(linea)


#5. Enunciado: Escribe el siguiente código y añade los comentarios necesarios para explicar su funcionamiento (difícil).
print(f"---Ejercicio nº 5: Asignación a una variable no declarada global")
def subrutina():
    d = e # AQUÍ SE CREA UNA VARIABLE LOCAL 'd' DENTRO DE LA FUNCIÓN 
    # No es necesario poner global porque no se está modificando ni d ni e de fuera de la función
    # esa d sólo existe dentro de la función, por eso imprime ahora 3, y luego 4
    print(d)
    return

d = 4 # Definición de variables
e = 3
subrutina()
print(d)

print(linea)

#6. Enunciado: Añade los comentarios necesarios para explicar el funcionamiento del código:
print(f"---Ejercicio nº 6: Explicar código")
def subrutina_1():
    f = 20
    print(f)
    return
def subrutina_2():
    global f
    f += 30 # le añadido la suma para ver si creaba una local
    print(f)
    return

f = 10 # comienza el programa con f valiendo 10
subrutina_1() # esta funcion crea una variable local f con valor 20 que imprime
print(f) # de regreso de la función, la f global no se ha modificado e imprime 10
subrutina_2() #Esta función sí modifica la variable global y la imprime en la función
print(f) # finalmente imprime la variable global con su valor modificado en la función

print(linea)

#7. Enunciado: Añade los comentarios necesarios para explicar el funcionamiento del código:
print(f"---Ejercicio nº 7: Explicar código")
def subrutina():
    def sub_subrutina():
        g = 5
        print(g)
        return
    g = 4
    sub_subrutina()
    print(g)
    return
g = 3
subrutina()
print(g)

print(linea)

#8. Enunciado: Escribe una función repite_hola que reciba como parámetro un número entero n y
#escriba por pantalla el mensaje "Hola"nveces.
print(f"---Ejercicio nº 8: XX")


print(linea)

#9. Enunciado: Escribe una función repite_saludo que reciba como parámetro un número entero n y una
#cadena saludo y escriba por pantalla el valor de saludo n veces.
print(f"---Ejercicio nº 9: XX")


print(linea)



#10. Enunciado: Define la función print_asegundos(horas, minutos, segundos) con tres parámetros (horas,
#minutos y segundos) que imprima por pantalla la transformación a segundos de una
#medida de tiempo expresada en horas, minutos y segundos:
print(f"---Ejercicio nº 10: XX")


print(linea)
