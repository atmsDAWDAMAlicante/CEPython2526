# EJERCICIOS - 01- Modulo - 01
# Ejercicios de Python Sintaxis
import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Pide al usuario su nombre completo y muestra el mensaje: Encantado de conocerte <nombre>
print(f"---Ejercicio nº 1: saludo")
nombre_completo = input("Introduce tu nombre completo: ")
print(f'Encantado de conocerte, {nombre_completo}')
print(f"{linea}")


#2. Realiza un programa que introduciéndole los kilómetros/hora me calcule los metros/segundo.
# Fórmula: hay que multiplicar por 1000 metros y dividir por 3600 segundos
print(f"---Ejercicio nº 2: km/h a m/s")
kilometros_hora = float(input("Introduce un número (Km/h): "))
metros_segundo = ((kilometros_hora*1000)/(3600))
print(f'{kilometros_hora} Km/h son {metros_segundo} Metros/segundo') # 45 Km/h = 12.5 m/s
print(f"{linea}")


#3. Solicita una cantidad a hipotecar y un interés anual (%), y calcula el pago anual con la fórmula: 
# pago = cantidad * interés.
print(f"---Ejercicio nº 3: cuota de préstamo hipotecario")
principal = float(input("Introduce la cantidad correspondiente al principal: "))
interes = float(input("Introduce la cantidad correspondiente al interés %: "))
pago_anual = principal * (interes/100)
print(f'La cuota anual del préstamo hipotecario, (capital: {principal} € al {interes}% de interés) asciende a {pago_anual} €')
print(f"{linea}")


#4. Realiza un programa que calcule las raíces de un polinomio de 2º grado.
"""
Nota: un polinomio de 2º grado es de la siguiente:
ax2 + bx + c = 0.

y su formula
x = (-b +/- RAIZ CUADRADA de b2 - 4ac ) /2a

Leer los valores a, b y c. Aplicad la fórmula. Recordad que tiene dos soluciones.
"""
print(f"---Ejercicio nº 4: polinomio de 2º grado (funciona con 1-9-6)")
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
print(f"{linea}")


#5. Realiza un programa que lea una temperatura en grados centígrados y la pase a grados Kelvin, Farenheit, grados cochinillos y grados alubianos.
"""
ºK = ºC + 273
ºF = ºC * 9 / 5 + 32
ºCochinillos = ºC * 22 + 123 - 2 + ºC / ºK;
ºAlubianos = (ºC - ºCochinillos + ºF) / ºK;
"""
print(f"---Ejercicio nº 5: conversor de temperaturas Cº Fº Kº")
grados_celsius = float(input("Introduce una temperatura en grados Celsius: "))
grados_kelvin = grados_celsius + 273
grados_farenheit = ((grados_celsius * 9) /5) + 32
grados_cochinillos =  ((grados_celsius * 22) + 123) - (2 + (grados_celsius / grados_farenheit))
grados_alubianos = (grados_celsius - grados_cochinillos - grados_farenheit) / grados_kelvin
print(f'A {grados_celsius}º corresponden:')
print(f'{grados_farenheit:.2f}º Farenheit - {grados_kelvin:<5.2f}º Kelvin')
print(f'{grados_cochinillos:.2f}º Cochinillos - {grados_alubianos:<5.2f}º Alubianos')
print(f"{linea}")


#6. Realiza un programa que lea pulgadas y pase a pies, codos, varas, índi es, orejas y jamones.
"""
pies = pulgadas / 15 
codos = pies / 1.3 
varas = codos / 1.23
indices = pulgadas * 0.85 
orejas = pulgadas * 0.99 + 2
jamones = varas - 12 + (indices * orejas) / codos
"""
print(f"---Ejercicio nº 6: conversor de medidas pulgadas")
pulgadas = float(input("Introduce una medida en pulgadas: "))
pies = pulgadas / 15
codos = pies / 1.3
varas = codos / 1.23
indices = pulgadas * 0.85
orejas = (pulgadas * 0.99) + 2
jamones = ((varas - 12) + (indices * orejas)) / codos
print(f'A {pulgadas} corresponden: ')
print(f'pies: {pies:.2f} - codos: {codos:.2f}')
print(f'varas: {varas:.2f} - indices: {indices:.2f}')
print(f'orejas: {orejas:.2f} - jamones: {jamones:.2f}')
print(f"{linea}")


#7. Realiza un programa que calcule el área de un triángulo y un cuadrado.
print(f"---Ejercicio nº 7: área de un cuadrado y un triángulo")
lado = float(input("Introduce un número que sea el lado de un cuadrado y de un triángulo equilátero: "))
area_cuadrado = lado * lado # área del cuadrado = lado * lado
# Área del triángulo 
# Fórmula para calcular el area del triángulo = Raiz de 3 / 4 * lado al cuadrado
area_triangulo = (math.sqrt(3)/4) * pow(lado,2)
print(f'El área del cuadrado es: {area_cuadrado:.2f}\nEl área del triángulo es: {area_triangulo:.2f}')
print(f"{linea}")



#8. Pide al usuario su peso (kg) y estatura (m), calcula el Índice de Masa Corporal (IMC = peso / estatura²) y muestra el resultado redondeado a 2 decimales en el formato:
#Tu índice de masa corporal es <imc> redondeado con dos decimales.
print(f"---Ejercicio nº 8: cálculo del IMC")
peso = (float(input("Introduce tu peso en kg: ")))
estatura = (float(input("Introduce tu altura en metros (p.e: 1.79): ")))
imc = peso / pow(estatura,2)
print(f'Para un peso de {peso:.2f} kg y una estatura de {estatura:.2f} metros\ncorresponde una IMC de: {imc:.2f}')
print(f"{linea}")



#9. Solicita dos números enteros al usuario y muestra el cociente y el resto de su división en el formato:
#<n> entre <m> da un cociente <c> y un resto <r>.
print(f"---Ejercicio nº 9: división entera")
dividendo = int(input("Introduce el dividendo (número entero):"))
divisor = int(input("Introduce el divisor (número entero):"))
resultado_division_entera = divmod(dividendo, divisor)
print(f'{resultado_division_entera}')

print(f"{linea}")



#10. Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética:
# ((3+2)/(2*5)) AL CUADRADO
print(f"---Ejercicio nº 10: operación aritmética")



print(f"{linea}")



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")