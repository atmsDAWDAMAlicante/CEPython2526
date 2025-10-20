# EJERCICIOS - 01- Modulo - 02 - Segunda semana
# Ejercicios para la tutoría colectiva UD1 Segunda semana

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Escribir un programa que pregunte el nombre completo del usuario en la consola 
# y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
def ejercicio_01(nombre):
    print(f"---Ejercicio nº 1: Nombre en mayúsculas, minúsculas y la primera en mayúsuculas")
    resultado = []
    mayusculas = nombre.upper()
    minusculas = nombre.lower()
    tercera_opcion = minusculas[0].upper() + minusculas[1:]
    
    resultado.extend([mayusculas, minusculas, tercera_opcion])
    print(resultado)
    print(f"{linea}")
    return resultado


#2. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión 
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
# (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato 
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
def ejercicio_02(tfno):
    print(f"---Ejercicio nº 2: Teléfono sin prefijo")

    #resultado = tfno[4:13]
    resultado = tfno[4:-3]
    print(resultado)
    print(f"{linea}")
    return resultado


#3. Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
# y muestra por pantalla, el día, el nombre del mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el año se introduzca con 2 o 4 dígitos.
def ejercicio_03(fecha):
    print(f"---Ejercicio nº 3: Fecha de nacimiento")

    #Toma el día de los dos primeros dígitos de la fecha (ignora la barra)
    dia = fecha[:2]

    #Toma el año de los dos últimos dígitos de la fecha (ignora la barra)
    anyo = fecha[-2:]

    #Toma el mes de los dos dígitos de en medio
    mesNumero = fecha[3:-3]
    #Para convertir el número del mes en su equivalente en letra llama 
    #a la función devuelveMes y le pasa el número de mes
    mes = devuelveMes(int(mesNumero))
    print(f"{linea}")
    return f'{dia} de {mes} de {anyo}'


def devuelveMes(num):
    #La función devuelveMes recibe el número de mes y devuelve el string correspondiente
    #a la posición de la tupla (número de mes - 1)
    mesLetras = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto", \
                 "Septiembre", "Octubre", "Noviembre", "Diciembre")
    return f'{mesLetras[num- 1]}'

#4. Ampliar el programa anterior para que acepte tres idiomas.
def ejercicio_04(fecha, lengua):
    print(f"---Ejercicio nº 4: Fecha de nacimiento entres idiomas")
    #Toma el día de los dos primeros dígitos de la fecha (ignora la barra)
    dia = fecha[:2]

    #Toma el año y el mes en función de la longitud del string que recibe la función
    #por parámetro. Si es mayor que diez caracteres se considera que el año tiene 4 dígitos
    if (len(fecha)<10):
        anyo = fecha[-2:]
        mesNumero = fecha[3:-3]
    else:
        anyo = fecha[-4:]
        mesNumero = fecha[3:-5]

    

    mes = devuelveMesLan(int(mesNumero), int(lengua))
    print(f'{dia} de {mes} de {anyo}')
    print(f"{linea}")
    return f'{dia} de {mes} de {anyo}'


def devuelveMesLan(num, lengua):
    #La función devuelveMes recibe el número de mes y devuelve el string correspondiente
    #a la posición de la tupla (número de mes - 1)
    #La tupla se rellena con los valores correspondientes en función del segundo parámetro
    #que se recibe y que determina el idioma: español, inglés o alemán
    if (lengua == 0):
        mesLetras = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto", \
                 "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    elif (lengua == 1):     
        mesLetras = ["January", "February", "March", "April", "May", "June", "July", "August", \
                     "September", "October", "November", "December"]
    else:
        mesLetras = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", \
                     "September", "Oktober", "November", "Dezember"]
    return f'{mesLetras[num- 1]}' # sólo devuelve el mes en el idioma solicitado



#5. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla 
# si la contraseña introducida por el usuario coincide con la guardada en la variable 
# sin tener en cuenta mayúsculas y minúsculas.
def ejercicio_05(passwordPropuesta):
    print(f"---Ejercicio nº 5: Password")
    passwordUsuario = "VACACIONES"
    if (passwordPropuesta.upper() == passwordUsuario):
        return "Acceso permitido"
    else:
        return "Acceso denegado"


print(f"{linea}")


#6. Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo a si son mayores de edad o menores y el nombre. 
# El grupo A esta formado por 
# los menores de edad con un nombre anterior a la M 
# y los mayores de edad con un nombre posterior a la N 
# y # el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y edad, 
# y muestre por pantalla el grupo que le corresponde.
def ejercicio_06():
    print(f"---Ejercicio nº 6: Grupos de alumnos")


#Prueba de los ejercicios
ejercicio_01("aDoLfO")
ejercicio_02("+34-913724710-56")
ejercicio_03("09/07/70")
ejercicio_04("09/07/70", 1)
ejercicio_04("09/07/1970", 0)

print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")