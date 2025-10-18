# EJERCICIOS - 01- Modulo - 01
# Ejercicios de Python Sintaxis

#1. Pide al usuario su nombre completo y muestra el mensaje: Encantado de conocerte <nombre>

nombre_completo = input("Introduce tu nombre completo: ")
print(f'Encantado de conocerte, {nombre_completo}')

#2. Realiza un programa que introduciéndole los kilómetros/hora me calcule los metros/segundo.
# Fórmula: hay que multiplicar por 1000 metros y dividir por 3600 segundos
kilometros_hora = float(input("Introduce un número (Km/h): "))
metros_segundo = ((kilometros_hora*1000)/(3600))
print(f'{kilometros_hora} Km/h son {metros_segundo} Metros/segundo') # 45 Km/h = 12.5 m/s

#3. Solicita una cantidad a hipotecar y un interés anual (%), y calcula el pago anual con la fórmula: 
# pago = cantidad * interés.
principal = float(input("Introduce la cantidad correspondiente al principal: "))
interes = float(input("Introduce la cantidad correspondiente al interés %: "))
pago_anual = principal * (interes/100)
print(f'La cuota anual del préstamo hipotecario, (capital: {principal} € al {interes}% de interés) asciende a {pago_anual} €')

#4. Realiza un programa que calcule las raíces de un polinomio de 2º grado.
"""
Nota: un polinomio de 2º grado es de la siguiente:
ax2 + bx + c = 0.

y su formula
x = (-b +/- RAIZ CUADRADA de b2 - 4ac ) /2a

Leer los valores a, b y c. Aplicad la fórmula. Recordad que tiene dos soluciones.
"""
# Introducción de los coeficientes a, b, c
print("Introduce tres números float")
numero_a = float(input("Introduce el primer coeficiente 'a': "))
numero_b = float(input("Introduce el primer coeficiente 'b': "))
numero_c = float(input("Introduce el primer coeficiente 'c': "))

# Cálculo de x
# hay que importar un módulo
import math
#Cálculo de las dos x
para_calcular_en_la_raiz = (pow(numero_b,2))- 4 * numero_a * numero_c
divisor = 2 * numero_a
numero_x1 = ((numero_b * -1) + math.sqrt(para_calcular_en_la_raiz)) / divisor
numero_x2 = ((numero_b * -1) - math.sqrt(para_calcular_en_la_raiz)) / divisor
print(f'El número x1 es: {numero_x1}')
print(f'El número x2 es: {numero_x2}')

#5. Realiza un programa que lea una temperatura en grados centígrados y la pase a grados Kelvin, Farenheit, grados cochinillos y grados alubianos.
"""
ºK = ºC + 273
ºF = ºC * 9 / 5 + 32
ºCochinillos = ºC * 22 + 123 - 2 + ºC / ºK;
ºAlubianos = (ºC - ºCochinillos + ºF) / ºK;
"""
grados_celsius = float(input("Introduce una temperatura en grados Celsius: "))
grados_kelvin = grados_celsius + 273
grados_farenheit = ((grados_celsius * 9) /5) + 32
grados_cochinillos =  ((grados_celsius * 22) + 123) - (2 + (grados_celsius / grados_farenheit))
grados_alubianos = (grados_celsius - grados_cochinillos - grados_farenheit) / grados_kelvin
print(f'A {grados_celsius}º corresponden:')
print(f'{grados_farenheit:.2f}º F {grados_kelvin:<5.2f}º K')
print(f'{grados_cochinillos:.2f}º Cochinillos {grados_alubianos:<5.2f}º Alubianos')

#6. Realiza un programa que lea pulgadas y pase a pies, codos, varas, índi es, orejas y jamones.
"""
pies = pulgadas/15 
codos = pies/1.3 
varas = codos/1.23
índices = pulgadas* 0.85 
orejas = pulgadas* 0.99+ 2
jamones = varas – 12 + (índices * orejas) /codos
"""

#7. Realiza un programa que calcule el área de un triángulo y un cuadrado.



#8. Pide al usuario su peso (kg) y estatura (m), calcula el Índice de Masa Corporal (IMC = peso / estatura²) y muestra el resultado redondeado a 2 decimales en el formato:
#Tu índice de masa corporal es <imc> redondeado con dos decimales.




#9. Solicita dos números enteros al usuario y muestra el cociente y el resto de su división en el formato:
#<n> entre <m> da un cociente <c> y un resto <r>.




#10. Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética:
# ((3+2)/(2*5)) AL CUADRADO





print("====================================\nFin de los ejercicios de este bloque\n====================================")