import os
os.system("cls")
linea = "==========================================="
#Parametros args
# se paga con un arterisco
# args captura posiciones

def captura_args(*args):
    print(type(args))
    for i in args:
        print(f'{i} - {type(args)}')
    # Termina el bucle y se convierte en lista    
    args = list(args)
    print(type(args))
    args.append("Federico") #Como lista, se le añade otro
    print(args)
captura_args("Pepe", "Juan", "Antonio", "Loli", "Paca")

'''
Explicación del ChatGPT
Ejemplo 3: Crear un string antes y luego pasarlo como *args

Esto solo tiene sentido si quieres dividirlo por algo.
Si lo pasas tal cual, será un único argumento:

cad = "uno dos tres"
unir(*cad.split())

Salida:
uno dos tres

.split() separa por espacios → devuelve lista → * la despliega en argumentos.

Entonces, respondiendo tu pregunta:
✔ ¿Se puede formar un string y pasarlo como *args?
Sí, siempre que lo desempaquetes o lo transformes adecuadamente:

funcion(*mi_string) → pasa cada carácter como argumento
funcion(*mi_string.split()) → pasa cada palabra

funcion(mi_string) → pasa un único argumento, el string completo
Mini resumen
Lo que haces	Lo que recibe *args
funcion("hola")	("hola",)
funcion(*"hola")	('h','o','l','a')
funcion(*"hola mundo".split())	("hola","mundo")
    
'''

#EJERCICIOS DEL CHATGPT
# Ejercicios con *args
#🟢 Nivel 1 – Básico
os.system("cls")
print(f"NIVEL 1 - BÁSICO\n{linea}")
#1.1 - Crea una función mostrar_args que reciba *args y muestre cada elemento en una línea.
print("1.1 - Crea una función mostrar_args que reciba *args y muestre cada elemento en una línea.")
def uno_uno_basico(*args):
    for i in args:
        print(i)
uno_uno_basico("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
#1.2 - Crea una función contar_args que devuelva cuántos argumentos recibió.
print(f"{linea}\n1.2 - Crea una función contar_args que devuelva cuántos argumentos recibió.")
def uno_dos_basico(*args):
    print(len(args))

uno_dos_basico("a","e","i","o","u")
#1.3 - Haz una función sumar_todos que reciba números y devuelva su suma.

#1.4 - Llama a cualquiera de ellas pasando una lista, sin *, y observa qué ocurre.

#1.5  Repite llamándola con *lista y compara los resultados.


'''
🟡 Nivel 2 – Medio

Crea una función mayor(*args) que devuelva el mayor número recibido.

Crea una función convertir_en_lista(*args) que retorne una lista con los argumentos recibidos.

Crea concatenar_strings(*args) que reciba un número indeterminado de strings y los una en uno solo separados por espacios.

Llama a concatenar_strings pasando un string solo, luego un string con *, y luego un string con .split(). Explica la diferencia.

🔵 Nivel 3 – Avanzado

Crea una función filtrar_enteros(*args) que reciba datos mezclados y retorne solo los que sean int.

Crea una función agregar_valor_final(*args) que convierta args en lista, agregue un elemento extra y lo retorne.

Dada una lista de nombres, usa * para llamar a una función que los imprima numerados:

nombres = ["Pepe","Juan","Loli","Sara"]
# Resultado esperado:
# 1. Pepe
# 2. Juan
# ...


Crea una función que acepte *args con palabras y genere un acrónimo (ej: "Python", "Software", "Foundation" → PSF).

🧠 Reto final

Escribe una función procesar(*args) que haga lo siguiente:

Reciba un número indeterminado de argumentos

Separe los que sean números y sume solo esos

Una en un string los que sean cadenas

Devuelva un diccionario con:

{
    "suma_numeros": ...,
    "texto_unido": ...,
    "cantidad_argumentos": ...
}


📌 Objetivo: practicar tipos, iteración, tuplas y manipulación de *args.

Cuando quieras puedes enviarme tus soluciones y te doy feedback, o si prefieres te doy las soluciones paso a paso a medida que los intentes.

¿Quieres empezar por el Nivel 1 y me mandas tus resoluciones para revisarlas? 😊
    
    
    
    
    '''