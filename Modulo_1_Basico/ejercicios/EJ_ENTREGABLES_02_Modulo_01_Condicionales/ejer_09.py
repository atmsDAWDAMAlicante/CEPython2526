#EJERCICIOS NTREGABLES UD 02 - Modulo 01 - Condicionales
#Ejercicio nº 9
# ALUMNO: ANGEL TOMÁS MORENO SENÉN

#Enunciado: Escribe un programa que en primer lugar pregunte si se
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

print(f"---Ejercicio nº 9: ENTREGABLE: Áreas de Triángulos y Círuclos")
import math #NECESARIO PARA HACER LA RAIZ CUADRADA
area = 0 
resultado = ""

# INPUT para recoger la figura
figura = input("Introduce la figura cuya área hay que calcular\n[C - Círculo]\[T - Triángulo] ")
figura = figura.lower()


# Función que evalúa la figura
def figura_Area(figura):
    if (figura =="c"):
        resultado = circulo()
    elif (figura == "t"):
        resultado = triangulo()
    else:
        resultado = "Entrada no válida"
    return resultado

# Definción de de las funciones que calculan las áreas

# Función para calcular el área del círuclo
# recoge el radio de un input y retorna el string a imprimir por consola
def circulo():
    radio = float(input("Introduce el radio del círculo: "))
    area = math.pi * pow(radio,2)
    return f'Un círculo de radio {radio} tiene un área de {area}'

# Función para calcular el área del triángulo
# recoge la base y la altura de dos inputs y retorna el string a imprimir por consola
def triangulo():
    base = float(input("Introduce la base del trinángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area = (base*altura)/2
    return f'Un triángulo de base {base:.1f} y altura {altura:.1f} tiene un área de {area:.2f}'



resultado = figura_Area(figura)
print(resultado)






'''
Código del test con pytest:
def test_entregable_09():
    assert entregable_ejer_09.ejercicio_09(1,-2,2) == "Sin solución real"


'''
