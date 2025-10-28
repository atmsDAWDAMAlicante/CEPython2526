# EJERCICIOS - 02 - Modulo - 01 - Condicionales

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Enunciado: Escribe un programa que pida por teclado dos números enteros. A continuación, el programa
#debe calcular su división, escribiendo el cociente entero, en caso de que el resto no sea cero,
#habrá que mostrar también el valor del resto entero.
#Nota: Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.
'''
(14/5): La división no es exacta. Cociente: 2 Resto: 4
(20/4): La división es exacta. Cociente: 5
(20/0): No se puede dividir por 0
'''

print(f"---Ejercicio nº 1: Muestra cociente y resto")
def ejercicio_01(dividendo, divisor):
    #variables
    dividendo = float(dividendo)
    divisor = float(divisor)
    resultado = ""

    #Primer condicional: maneja la división por cero
    if (divisor == 0):
        resultado = "No se puede dividir por 0"
    else: 
        cociente = dividendo//divisor
        resto = dividendo%divisor
        #Segundo condicional: primero evalúa si la división es exacta
        if (resto == 0):
            resultado = f'La división es exacta. Cociente: {cociente}'
        else:
            resultado = f'La división no es exacta. Cociente: {cociente} Resto: {resto}'


    return resultado


print(f"{linea}")


#2. Enunciado: Escribe un programa que pida por teclado dos números y que indique cuál de ellos es el menor
#y cuál el mayor o bien si ambos números son iguales.
print(f"---Ejercicio nº 2: xxx")



print(f"{linea}")


#3. Enunciado: Escribe un programa que pida por teclado en primer lugar el año actual y después un año
#cualquiera. A continuación, el programa ha de indicar cuántos años faltan para llegar o
#cuantos años han pasado al/desde ese segundo año.
#Nota: Se puede mejorar el programa haciendo que cuando la diferencia sea
#exactamente un año escriba la frase en singular.
print(f"---Ejercicio nº 3: xxx")



print(f"{linea}")


#4. Enunciado: Escribe un programa que pida dos números enteros y que a continuación indique si el
#número mayor es múltiplo del menor.
print(f"---Ejercicio nº 4: xxx")



print(f"{linea}")


#5. Enunciado: Escribe un programa que pida tres números. El programa ha de indicar a continuación si
#estos tres valores son iguales, si dos de ellos son iguales o si son los tres distintos.
print(f"---Ejercicio nº 5: xxx")



print(f"{linea}")


#6. Enunciado: Escribe un programa que pida un año y que determine si ese año es bisiesto o no.
#Recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo
#son, aunque los múltiplos de 400 sí.
print(f"---Ejercicio nº 6: xxx")



print(f"{linea}")


#7. Enunciado: Escribe un programa que solicite los coeficientes de una ecuación de primer grado:
#(a.x + b =0), y que a continuación calcule y muestre como resultado la solución a la ecuación.
#Una ecuación de primer grado puede no tener solución, tener una solución única, o
#que todos los números sean solución. La fórmula de las soluciones es x = -b / a
#Estos son algunos ejemplos de posibles respuestas:
#a b Solución
#0 3 Sin solución
#4.2 21 Una solución: -5
#0 0 Todos los números son solución
print(f"---Ejercicio nº 7: xxx")



print(f"{linea}")


#8. ENTREGABLE - Enunciado: Escribe un programa que pida los coeficientes de una ecuación de
#segundo grado (a x² + b x+ c = 0) y que a continuación muestre la/s soluciones.
#Una ecuación de segundo grado puede no tener solución, tener una solución única,
#tener dos soluciones o que todos los números sean solución.
#Estos son algunos ejemplos de posibles respuestas:
'''
a b c Solución
1 -2 2 Sin solución real
2 -7 3 Dos soluciones: 0.5 y 3.0
1 2 1 Una solución: -1.0
0 0 5 Sin solución
0 0 0 Todos los números son solución
0 3 2 Una solución: -0.666…
'''

print(f"---Ejercicio nº 8: xxx")



print(f"{linea}")


#9. ENTREGABLE - Enunciado: Escribe un programa que en primer lugar pregunte si se
#quiere calcular el área de untriángulo o la de un círculo.
#Si se contesta que se quiere calcular el área de un triángulo, el programa tiene que pedir
#entonces la base y la altura y escribir el área.
#Si se contesta que se quiere calcular el área de un círculo, el programa tiene que pedir
#entonces el radio y escribir el área.
#En ambos casos el programa debe ser capaz de calcular y mostrar el resultado adecuado.
'''
Cálculo de áreas - Elige una figura geométrica:
    a) Triángulo
    b) Círculo
    ¿Qué figura quieres calcular (Escribe T o C)? T
        Escribe la base: 3
        Escribe la altura: 5.5
    Un triángulo de base 3.0 y altura 5.0 tiene un área de 8.25
Cálculo de áreas - Elige una figura geométrica:
    a) Triángulo
    b) Círculo
    ¿Qué figura quieres calcular (Escribe T o C)? C
        Escribe el radio: 2
        Un círculo de radio 2.0 tiene un área de 12.566370614359172
'''
print(f"---Ejercicio nº 9: xxx")



print(f"{linea}")


#10. Enunciado: Escribe un programa que pida una distancia en centímetros y que Escribe esa distancia en
#kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).
'''
Distancia en cm Distancia en km, m y cm
    100         1 m
    240005      2 km, 400 m, 5 cm
    67          67 cm
    300004      3 km, 4 cm
La dificultad del ejercicio se puede reducir o aumentar según la forma de presentar el
resultado:
    ▪ sin separador entre unidades: 2 km 400 m 5 cm
    ▪ separando con comas las unidades: 2 km, 400 m, 5 cm
    ▪ separando con comas y con la conjunción 'y' en la última unidad: 2 km, 400 m y 5 cm

Convertidor de centímetros a kilómetros, metros y centímetros
Escribe una distancia en centímetros: 43210
43210 centímetros son 432 m, 10 cm.
'''
print(f"---Ejercicio nº 10: xxx")



print(f"{linea}")


#11. ENTREGABLE - Enunciado:
'''
Realiza un programa que pida:
    • El nombre del usuario
    • Su edad
    • Su ingreso anual (€)
El programa debe aplicar las siguientes reglas:
    1. Si la edad es menor de 18 → no paga impuestos.
    2. Si tiene entre 18 y 65 años:
        o Si gana menos de 15.000 €, paga un 5 % de impuestos.
        o Entre 15.000 € y 30.000 €, paga un 10 %.
        o Entre 30.000 € y 60.000 €, paga un 20 %.
        o Más de 60.000 €, paga un 30 %.
    3. Si tiene más de 65 años, se le aplica un descuento del 50 % sobre el impuesto
    correspondiente.
    4. Si su nombre empieza por “A” o “a”, obtiene un bono adicional de -2 % (descuento).
    5. El programa mostrará:
        El impuesto base aplicado
        El descuento (si procede)
        El impuesto final a pagar
        Un mensaje personalizado con su nombre y edad.
'''
print(f"---Ejercicio nº 11: xxx")



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")