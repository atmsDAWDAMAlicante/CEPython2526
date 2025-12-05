# EJERCICIOS - 02 - Modulo - 02 - Diccionarios
# Diccionarios: Bloque de ejercicios progresivos. Es obligatorio incluir comentarios en todos ellos.

import os

class ErrorPersonalizado(Exception):
    pass

linea = "===================================="
def limpiar_consola():
    try:
        os.system('clear')
    except ErrorPersonalizado:
        os.system('cls')   

limpiar_consola()
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

# En principio creo el diccionario como indica el enunciado, 
# siendo la clave el dorsal y el nombre el valor
print(f"---Ejercicio nº 1: Diccionario de titulares:\n")
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
try:
    print(titulares["2"]) # el 2 no está aún
except KeyError:
    print(f"El dorsal 2 no está en el diccionario de titulares\n")

titulares["100"] = "Manolo el del Bombo"
print(titulares)
titulares.pop("100")
print(titulares.get("100","Manolo el del Bombo no es un titutlar")) # con get no da error si no existe la clave

print(f"{linea}")
#2. Enunciado: Utilizando la función get() muestra de forma tabulada y ordenados por su número dorsal
#de menor a mayor los nombres de los once jugadores (el menor dorsal posible es el 1 y
#nunca podrá tener más de dos cifras.

print(f"---Ejercicio nº 2: Mostrar tabulada la Selección Nacional:\n")
titulares_ordenados = titulares.copy()
titulares_ordenados = dict(sorted(titulares_ordenados.items()))
print (type(titulares_ordenados))
#print ("Titulares: ", id(titulares_ordenados))
for clave,valor in titulares_ordenados.items():
    print(f"{clave:<10} - {valor:<20}")

print(f"{linea}")
#3. Enunciado: Modifica el ejercicio anterior para que programa lea el número de elementos incluidos en
#el diccionario titulares, mostrando ese valor mediante la expresión ‘Iniciaron el partido XX
#jugadores’, siendo XX el número de elementos incluidos en el diccionario.
'''
¡¡¡Este ejercicio no lo entieno!!!
'''
print(f"---Ejercicio nº 3: Mostrar la Selección Nacional y recuento:\n")
num_jugadores = len(titulares)
print(f"Iniciaron el partido {num_jugadores} jugadores, siendo {len(titulares)} el número de elementos incluidos en el diccionario")
for clave,valor in titulares_ordenados.items():
    print(f"{clave:<10} - {valor:<20}")

#print(f"---Ejercicio nº 3: Recuento general")


#4. Enunciado: Añade al ejercicio anterior el código necesario mostrar una lista con todos los índices
#utilizados en la biblioteca y otra lista con todos los valores almacenados en ella (utiliza
#los métodos Name.keys() y Name.values())
print(f"---Ejercicio nº 4: Formando una lista de dorsales y otra de jugadores:\n")
dorsales = list(titulares_ordenados.keys())
print("Lista de dorsales:", dorsales)
jugadores = list(titulares_ordenados.values())
print("Lista de jugadores:", jugadores)
try:
    print(titulares_ordenados["100"]) # el 50 no está aún
except KeyError:
    print(f"¡Qué Manolo el del Bombo no está!\n")
print(f"{linea}")

#5. Enunciado: Partimos ahora del ejercicio 1. Añade el código necesario para que el programa cree una
#copia de la biblioteca “titulares” y asígnale el nombre plantilla. Muestra por pantalla el
#contenido de plantilla con el mismo formato que el indicado en el ejercicio 2.
print(f"---Ejercicio nº 5: Copia de la biblioteca titulares")
plantilla = titulares_ordenados.copy()
for clave,valor in plantilla.items():
    print(f"{clave:<10} - {valor:<20}")
print(f"{linea}")
#6. Enunciado: Añade al programa un nuevo diccionario al que llamaremos suplentes. Los elementos de
#dicho diccionario serán los once jugadores suplentes el día del partido, siendo el número
#de su dorsal el índice y su nombre el valor asociado. Muestra como resultado el
#contenido de los dos diccionarios siguiendo el mismo formato que en los ejercicios 2 y 5.
#print(f"---Ejercicio nº 6: Suplentes")
suplentes = {
    23: "Pepe Reina",
    12: "Víctor Valdés",
    4: "Marchena",
    17: "Arbeloa",
    20: "J. Martínez",
    22: "Jesús Navas",
    2: "Raúl Albiol",
    21: "David Silva",
    10: "Cesc Fàbregas",
    13: "J.Mata",
    9: "Fernando Torres",
    19: "F. Llorente" 
}


print(f"{linea}")


#7. Enunciado: A partir del anterior añade los elementos del diccionario suplentes al diccionario plantilla
#y muestra el contenido actualizado del diccionario plantilla siguiendo el formato de los ejercicios anteriores.

print(f"---Ejercicio nº 7: Unir plantilla y suplentes")
# Voy a poner toda la seleccion en un único diccionario el diccionario titutlares
plantilla = titulares.copy()
plantilla.update(suplentes)
plantilla = dict(sorted(plantilla.items())) # y lo ordeno
for clave,valor in plantilla.items():
    print(f"{clave:<10} - {valor:<20}")
print("Vamos a ver los tipos")
print(type(plantilla))
print(type(titulares))
print(type(suplentes))
print(f"{linea}")


#8. ENTREGABLE - Enunciado: Una vez hecho todo lo anterior ten en cuenta que durante el
#partido se produjeron tres sustituciones. Xabi Alonso, Pedrito y Villa abandonaron el
#campo. Navas, Fàbregas y Torres se incorporaron. Haz una copia del diccionario
#“titulares” y asígnale el nombre “final”. Utilizando los métodos setdefault(key,valor) y
#pop(key), elimina del diccionario final a los tres jugadores que fueron sustituidos y añade
#a los que se incorporaron. Muestra al final del ejercicio el contenido del diccionario final
#con el formato de los ejercicios anteriores.
#print(f"---Ejercicio nº 8: Cambios de los titulares")

# Copia del diccionario titutulares
final = titulares.copy()

#Los que salen
final.pop(14) # Xabi Alonso
final.pop(18) # Pedrito
final.pop(7)  # Villa
#Los que entran
final.setdefault(22, "Jesús Navas")   # Navas
final.setdefault(10, "Cesc Fàbregas")  # Fàbregas
final.setdefault(9, "Fernando Torres") # Torres
print(f"ALINEACIÓN FINAL:")
final = dict(sorted(final.items()))
for clave,valor in final.items():
    print(f"{clave:<10} - {valor:<20}")




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
print(f"---Ejercicio nº 9: Buscar por dorsal o por nombre")

def menu_busqueda():
    mneu = input("Introduce 1 para dorsal, 2 para nombre otro para salir: ")
    while True:
        try:
            opcion = int(mneu)
            if opcion == 1:
                    pass
                    #operacion(1)
            elif opcion == 2:
                    pass
                    #operacion(2)
            else:
                    print("Salida.")
                    break
                    
        except ValueError:
            print("Saliendo de la búsqueda.")
        mneu = input("Introduce BIEN 1 para dorsal, 2 para nombre otro para salir: ")
       
menu_busqueda()
print(f"{linea}")


#10. ENTREGABLE - Enunciado: VAMOS A POR EL DIEZ: Ahora tú eres el seleccionador y vas a hacer los cambios.
#Partimos de los diccionarios titulares y suplentes. El programa mostrará las dos listas
#con el formato habitual. A continuación te preguntará por el número del primer
#jugador que quieres sustituir. Tras contestar, el programa preguntará por el número
#del jugador que quieres que entre en su lugar. Ten en cuenta que el jugador
#que ha sido sustituido no puede volver a entrar al campo. A continuación se
#mostrarán los contenidos actualizados de los dos diccionarios. Ten en cuenta que podemos hacer un máximo de tres cambios
#print(f"---Ejercicio nº 10: xxx")
print(titulares)
print(suplentes)
print(plantilla)


print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")