# EJERCICIOS - 02 - Modulo - 02 - Diccionarios
# Diccionarios: Bloque de ejercicios progresivos. Es obligatorio incluir comentarios en todos ellos.

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Enunciado: El 11 de julio de 2010 la selección española de fútbol gano su primer y único mundial. La
#alineación titular fue la siguiente:
'''
1 POR Iker Casillas Capitán
15 DEF Sergio Ramos
3 DEF Gerard Piqué
5 DEF Carles Puyol
11 DEF Joan Capdevila
14 MED Xabi Alonso
16 MED Sergio Busquets
8 MED Xavi Hernández
18 MED Pedro Rodríguez
6 MED Andrés Iniesta
7 DEL David Villa
'''
#Crea un diccionario al que llamaremos titulares. Los elementos de dicho diccionario serán
#los once jugadores que comenzaron el partido, añadidos en el orden mostrado en la tabla
#anterior, siendo el número de su dorsal el índice y su nombre el valor asociado.

# En principio creo el diccionario como indica el enunciado, siendo la clave el dorsal y el nombre el valor
print(f"---Ejercicio nº 1: Diccionario de titulares")
titulares = {
1: "Iker Casillas",
15: "Sergio Ramos",
3: "Gerard Piqué",
5: "Carles Puyol",
11: "Joan Capdevila",
14: "Xabi Alonso",
16: "Sergio Busquets",
8: "Xavi Hernández",
18: "Pedro Rodríguez",
6: "Andrés Iniesta",
7: "David Villa"
}


print(f"{linea}")


#2. Enunciado: Utilizando la función get() muestra de forma tabulada y ordenados por su número dorsal
#de menor a mayor los nombres de los once jugadores (el menor dorsal posible es el 1 y
#nunca podrá tener más de dos cifras.
os.system("clear")
print(f"---Ejercicio nº 2: Mostrar tabulada la Selección Nacional")

resultado_ordenado = sorted(titulares.items())
print (resultado_ordenado)
for dorsal, jugador in sorted(titulares.items()):
    #print(f'{dorsal} - {jugador}')
    print(dorsal, jugador, sep = " - ")

print(f"{linea}")


#3. Enunciado: Modifica el ejercicio anterior para que programa lea el número de elementos incluidos en
#el diccionario titulares, mostrando ese valor mediante la expresión ‘Iniciaron el partido XX
#jugadores’, siendo XX el número de elementos incluidos en el diccionario.
'''
¡¡¡Este ejercicio no lo entieno!!!
'''
print(f"---Ejercicio nº 3: Recuento general")
titulares_De_La_Seleccion = len(titulares)
titulares_Del_Diccionario = len(titulares)
print(f'‘Iniciaron el partido {titulares_De_La_Seleccion} jugadores, siendo {titulares_Del_Diccionario} el número de elementos incluidos en el diccionario')

print(f"{linea}")


#4. Enunciado: Añade al ejercicio anterior el código necesario mostrar una lista con todos los índices
#utilizados en la biblioteca y otra lista con todos los valores almacenados en ella (utiliza
#los métodos Name.keys() y Name.values())
print(f"---Ejercicio nº 4: xxx")



print(f"{linea}")


#5. Enunciado: Partimos ahora del ejercicio 1. Añade el código necesario para que el programa cree una
#copia de la biblioteca “titulares” y asígnale el nombre plantilla. Muestra por pantalla el
#contenido de plantilla con el mismo formato que el indicado en el ejercicio 2.
print(f"---Ejercicio nº 5: Copia de la biblioteca titulares")



print(f"{linea}")


#6. Enunciado: Añade al programa un nuevo diccionario al que llamaremos suplentes. Los elementos de
#dicho diccionario serán los once jugadores suplentes el día del partido, siendo el número
#de su dorsal el índice y su nombre el valor asociado. Muestra como resultado el
#contenido de los dos diccionarios siguiendo el mismo formato que en los ejercicios 2 y 5.
print(f"---Ejercicio nº 6: xxx")



print(f"{linea}")


#7. Enunciado: A partir del anterior añade los elementos del diccionario suplentes al diccionario plantilla
#y muestra el contenido actualizado del diccionario plantilla siguiendo el formato de los ejercicios anteriores.
print(f"---Ejercicio nº 7: xxx")



print(f"{linea}")


#8. ENTREGABLE - Enunciado: Una vez hecho todo lo anterior ten en cuenta que durante el
#partido se produjeron tres sustituciones. Xabi Alonso, Pedrito y Villa abandonaron el
#campo. Navas, Fàbregas y Torres se incorporaron. Haz una copia del diccionario
#“titulares” y asígnale el nombre “final”. Utilizando los métodos setdefault(key,valor) y
#pop(key), elimina del diccionario final a los tres jugadores que fueron sustituidos y añade
#a los que se incorporaron. Muestra al final del ejercicio el contenido del diccionario final
#con el formato de los ejercicios anteriores.
print(f"---Ejercicio nº 8: xxx")



print(f"{linea}")


#9. ENTREGABLE - Enunciado: Partiendo del programa anterior (con los diccionarios titulares,
#suplentes, plantilla y final ya creados):
#Añade un bloque de código que permita al usuario buscar información sobre los jugadores.
#El programa deberá ofrecer dos opciones:
'''
    Opción 1: Buscar jugador por su número de dorsal.
    Si el dorsal existe, mostrará el nombre del jugador y si fue titular, suplente o jugó la final.
    Opción 2: Buscar jugador por su nombre o parte del nombre (no distingue mayúsculas/minúsculas).
'''
#Si el nombre coincide con alguno en la plantilla, se mostrará el dorsal y si fue titular, suplente o jugó la final.
#Si se introduce una opción distinta de 1 o 2, el programa mostrará el mensaje "Opción no válida."
print(f"---Ejercicio nº 9: xxx")



print(f"{linea}")




#10. ENTREGABLE - Enunciado: VAMOS A POR EL DIEZ: Ahora tú eres el seleccionador y vas a hacer los cambios.
#Partimos de los diccionarios titulares y suplentes. El programa mostrará las dos listas
#con el formato habitual. A continuación te preguntará por el número del primer
#jugador que quieres sustituir. Tras contestar, el programa preguntará por el número
#del jugador que quieres que entre en su lugar. Ten en cuenta que el jugador
#que ha sido sustituido no puede volver a entrar al campo. A continuación se
#mostrarán los contenidos actualizados de los dos diccionarios. Ten en cuenta que podemos hacer un máximo de tres cambios
print(f"---Ejercicio nº 10: xxx")



print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")