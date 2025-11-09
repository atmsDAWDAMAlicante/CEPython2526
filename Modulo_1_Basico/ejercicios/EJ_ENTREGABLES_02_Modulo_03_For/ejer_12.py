#EJERCICIOS NTREGABLES UD 02 - Modulo 03 - For
#Ejercicio nº 12
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

#Enunciado: 
#def ejercicio_12(num):

print(f"---Ejercicio nº 12: Entregable: numeros Perfectos, Deficientes, Abundantes o Amigos")
num = int(input("Introduce un número entero: "))
#Variables globales
mensaje_ej_12 = "" #Aquí se recogerá el string que se imprimirá por pantalla 
suma_divisores = 0 # int encargado de sumar los divisores
lista_de_divisores = [] #Esta lista recoge individualmente los divisores
tipo_numero = ("PERFECTO", "DEFICIENTE", "ABUNDANTE", "AMIGO") #Tupla con los nombres de los tipos de números
num_amigo = 0 # Numero amigo pendiente de calcular

#A) PRIMERA PARTE: el bucle que identifica los divisores, los introduce en la lista y los suma

for i in range(1, num+1): #Bucle desde 1 (para evitar la división por 0) hasta el número pasado +1
    if (num%i == 0) and (i < num): # Evalúa que no haya resto Y que el contador sea menor al número pasado
        suma_divisores += i # Se suma i que es el divisor que cumple la condición
        lista_de_divisores.append(i) # y se añade a la lista de divisores

#Aquí se genera la primera parte del fstring que se mostrará como resultado
mensaje_ej_12 = f"Divisores propios: {lista_de_divisores}\nSuma de divisores: {suma_divisores}"

#B) SEGUNDA PARTE: El tipo de número 

if (num == suma_divisores):
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
    # En caso contrario... se introduce un nuevo condicional que, ahora sí discrimina si es deficiente o abundante
    else:
        if (num > suma_divisores):
            mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[1]}."
        else:
            mensaje_ej_12 += f"\nEl número {num} es {tipo_numero[2]}."


# SALIDA FINAL
print(mensaje_ej_12)

#return mensaje_ej_12

'''
Tests:
#Para la realización de la primera parte del ejercicio 12

def test_ejercicio12():
    assert mod2_eje3.ejercicio_12(28) == "Divisores propios: [1, 2, 4, 7, 14]\nSuma de divisores: 28"
    assert mod2_eje3.ejercicio_12(12) == "Divisores propios: [1, 2, 3, 4, 6]\nSuma de divisores: 16"
    assert mod2_eje3.ejercicio_12(220) == "Divisores propios: [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]\nSuma de divisores: 284"

#Para la realización del ejercicio 12 completo
def test_ejercicio12():
    assert mod2_eje3.ejercicio_12(28) == "Divisores propios: [1, 2, 4, 7, 14]\nSuma de divisores: 28\nEl número 28 es PERFECTO."
    assert mod2_eje3.ejercicio_12(12) == "Divisores propios: [1, 2, 3, 4, 6]\nSuma de divisores: 16\nEl número 12 es ABUNDANTE."
    assert mod2_eje3.ejercicio_12(220) == "Divisores propios: [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]\nSuma de divisores: 284\nEl número 220 es AMIGO del número 284."

'''