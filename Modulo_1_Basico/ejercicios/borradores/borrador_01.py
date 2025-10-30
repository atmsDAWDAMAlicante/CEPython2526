import os

linea = "===================================="
os.system('cls')
print("Hola mundo")
a: int = 4
b = "Hola"
c = 4
print(b+str(c))
"""
Comentario de
 varias líneas
"""
print(abs(-3.1416))

nom1 = "Don Pepito"
nom2 = "Don José"
lugar1 = "casa"
persona1 = "abuela"
print(f'Hola, {nom1}\nHola, {nom2}\n¿Pasó usted por mi {lugar1}?')

valor1 = 1234567890
print(f'{valor1:.2f}')
print(f'{valor1:1d} - {valor1:2d}')

divisionentera = divmod(342423,565)
print(divisionentera) #(606, 33)
print(pow(2,3))

#Dos números
num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))
if (num1 > num2):
    print(f'{num1} es mayor que {num2}')
elif (num1 < num2):
    print(f'{num1} es menor que {num2}')
else:
    print("Dos iguales para hoy")

#Par/Impar
num_par_impar = int(input("Introduce un número para evaluar si es par o impar: "))
if (num_par_impar%2 == 0):
    print(f'{num_par_impar} es par')
else:
    print(f'{num_par_impar} es impar')

#Nota alumno
nota_alumno = float(input("Introduce la nota del alumno: "))
if (nota_alumno >= 0) and (nota_alumno <=2):
    print(f'La nota {nota_alumno} tiene una calificación: Muy Deficiente')
elif (nota_alumno >= 3) and (nota_alumno <=4):
    print(f'La nota {nota_alumno} tiene una calificación: Insuficiente')
elif (nota_alumno >= 5) and (nota_alumno <=6):
    print(f'La nota {nota_alumno} tiene una calificación: Aprobado')
elif (nota_alumno >= 7) and (nota_alumno <=8):
    print(f'La nota {nota_alumno} tiene una calificación: Notable')
elif (nota_alumno >= 9) and (nota_alumno <=10):
    print(f'La nota {nota_alumno} tiene una calificación: Sobresaliente')
else:
    print("Error")