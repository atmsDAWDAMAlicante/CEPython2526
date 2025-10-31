#EJERCICIOS NTREGABLES UD 02 - Modulo 01 - Condicionales
#Ejercicio nº 8
# ALUMNO: ANGEL TOMÁS MORENO SENÉN

#Enunciado: Escribe un programa que pida los coeficientes de una ecuación de #segundo grado (a x² + b x+ c = 0) 
# y que a continuación muestre la/s soluciones.
# 
# #Una ecuación de segundo grado puede no tener solución, tener una solución única, #tener dos soluciones o que todos los números sean solución.

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

# 2º Posibilidad
# Utilizando la tabla de verdad del DISCRIMINANTE (ha habido que buscar la fórmula)
# (ver abajo la 1º Posibilidad: que falla en un supuesto)
# DISCRIMINANTE o D = b^2 - 4ac
# En base a esta fórmula se establece la siguiente tabla de verdad:
'''
1.- Evaluando si a y b = 0
    C = 0 # "Todos los números son solución"
    C != 0 # "Sin solución"
2.- Evaluando si a = 0 y b != 0 # Una solución: -0.666… - HAY QUE CALCULAR D
3.- Evaluando el D
    D < 0 # "Sin solución real"
    D > 0 # f'Las soluciones de la ecuación son {numero_x1:.1f} y {numero_x2:.1f}'
    D = 0 # Una solución: -0.666… esta se repite con el 2.-
    
''' 

print(f"---Ejercicio nº 8: ENTREGABLE: Ecuación de segundo grado")
import math #NECESARIO PARA HACER LA RAIZ CUADRADA

# INPUTS
numero_a = input("Introduce un primer número: ")
numero_b = input("Introduce un segundo número: ")
numero_c = input("Introduce un tercero número: ")
numero_a = float(numero_a)
numero_b = float(numero_b)
numero_c = float(numero_c)
# Función que evalúa los datos introducidos

def ejercicio_08(numero_a, numero_b, numero_c):
    resultado = "" # RECOGERÁ EL MENSAJE QUE SE DEVUELVE

    if (numero_a == 0) and (numero_b == 0): # ESTE IF EVALUA EL PUNTO 1 DE LA TABLA DE VERDAD
        if (numero_c == 0): # C = 0 # "Todos los números son solución"
            resultado = "Todos los números son solución"

        else: # C != 0 # "Sin solución"
            resultado = "Sin solución"
    else: # A PARTIR DE AQUÍ SE EVALÚAN LOS PUNTOS 2 Y 3 DE LA TABLA DE VERDAD
        d = operacion_Discriminante(numero_a, numero_b, numero_c) # LLAMA A OTRA FUNCIÓN
        divisor = 2 * numero_a # Para tener el divisior en una variable y que se vea mejor
        if (d < 0): # Primero se evalúa el punto 3.1 de la tabla de la verdad
            resultado = "Sin solución real"
        else: # Ahora se evalúan los demás puntos que implican realizar la operación completa
            numero_x1 = (((numero_b * -1) + math.sqrt(d)) / divisor)
            numero_x2 = (((numero_b * -1) - math.sqrt(d)) / divisor)
            # Estos condicionales elaboran la respuesta con literales obtenidos de las operaciones
            if (d == 0):
                resultado =f'Una solución: {numero_x1:.2f}'
            else:
                resultado = f'Las soluciones de la ecuación son {numero_x1:.1f} y {numero_x2:.1f}'

    return resultado

def operacion_Discriminante(numero_a, numero_b, numero_c):
    resultado_operacion = (pow(numero_b,2)-(4 * numero_a * numero_c))
    return resultado_operacion

print(ejercicio_08(numero_a, numero_b, numero_c))
'''
Código del test con pytest:
def test_entregable_08():
    assert entregable_ejer_08.ejercicio_08(1,-2,2) == "Sin solución real"
    assert entregable_ejer_08.ejercicio_08(0,0,5) == "Sin solución"
    assert entregable_ejer_08.ejercicio_08(0,0,0) == "Todos los números son solución"
    assert entregable_ejer_08.ejercicio_08(2,-7,3) == "Las soluciones de la ecuación son 3.0 y 0.5"
    assert entregable_ejer_08.ejercicio_08(1,2,1) == "Una solución: -1.00"

'''


# 1º Posibilidad: CONTIENE UN ERROR LÓGICO EN LA TABLA DE VERDAD UTILIZADA
# (a > b) and (b < c) return "Sin solución real"
# (a == b) and (b < c) return "Sin solución"
# (a == b == c) return "Todos los números son solución"
# (a > b) and (b > c) return "Dos soluciones: x1 y x2"
# (a < b) and (b > c) return "Una solución x"
'''

print(f"---Ejercicio nº 8: ENTREGABLE: Ecuación de segundo grado")
import math #NECESARIO PARA HACER LA RAIZ CUADRADA

def ejercicio_08(numero_a, numero_b, numero_c):
    resultado = "" # RECOGERÁ EL MENSAJE QUE SE DEVUELVE

    if (numero_a > numero_b) and (numero_b < numero_c):
        resultado = "Sin solución real"
    elif (numero_a == numero_b) and (numero_b < numero_c):
        resultado = "Sin solución"
    elif (numero_a == numero_b == numero_c):
        resultado = "Todos los números son solución"
    else: # Ahora se calcula la ecuación
        para_calcular_en_la_raiz = (pow(numero_b,2))- 4 * numero_a * numero_c
        divisor = 2 * numero_a
        numero_x1 = (((numero_b * -1) + math.sqrt(para_calcular_en_la_raiz)) / divisor)
        numero_x2 = (((numero_b * -1) - math.sqrt(para_calcular_en_la_raiz)) / divisor)
        
        resultado = f'Las soluciones de la ecuación son {numero_x1:.1f} y {numero_x2:.1f}'


    return resultado

'''