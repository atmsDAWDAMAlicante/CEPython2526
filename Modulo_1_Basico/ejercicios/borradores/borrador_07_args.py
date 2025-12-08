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
#📌 Objetivo: practicar tipos, iteración, tuplas y manipulación de *args.

#🟢 Nivel 1 – Básico
os.system("cls")
print(f"NIVEL 1 - BÁSICO\n{linea}")
#1.1 - Crea una función mostrar_args que reciba *args y muestre cada elemento en una línea.
print("1.1 - Crea una función mostrar_args que reciba *args y muestre cada elemento en una línea.")
def mostrar_args(*args):
    for i in args:
        print(i)
mostrar_args("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
#1.2 - Crea una función contar_args que devuelva cuántos argumentos recibió.
print(f"{linea}\n1.2 - Crea una función contar_args que devuelva cuántos argumentos recibió.")
def contar_args(*args):
    print(len(args))

contar_args("a","e","i","o","u")

#1.3 - Haz una función sumar_todos que reciba números y devuelva su suma.
print(f"{linea}\n1.3 - Haz una función sumar_todos que reciba números y devuelva su suma.")
def sumar_todos(*args):
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)
sumar_todos(10,20,30,40,50)

#1.4 - Llama a cualquiera de ellas pasando una lista, sin *, y observa qué ocurre.
print(f"{linea}\n1.4 - Llama a cualquiera de ellas pasando una lista, sin *, y observa qué ocurre.")
'''
def sumar_todos2(args):
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)
sumar_todos2(10,20,30,40,50)
'''
#1.5  Repite llamándola con *lista y compara los resultados.
print(f"{linea}\n1.5  Repite llamándola con *lista y compara los resultados.")
def sumar_todos3(*lista):
    resultado = 0
    for i in lista:
        resultado += i
    print(resultado)
sumar_todos3(10,20,30,40,50)


#🟡 Nivel 2 – Medio

#2.1  Crea una función mayor(*args) que devuelva el mayor número recibido.
print(f"{linea}\n2.1  Crea una función mayor(*args) que devuelva el mayor número recibido.")
def mayor(*args):
    el_mayor = 0
    for i in args:
        if i > el_mayor:
            el_mayor = i
    print(el_mayor)

mayor(1,3,4,5,34,523,423,4,456,234,234,3,800)
#2.2  Crea una función convertir_en_lista(*args) que retorne una lista con los argumentos recibidos.

#2.3  Crea concatenar_strings(*args) que reciba un número indeterminado de strings y los una en uno solo separados por espacios.

#2.4  Llama a concatenar_strings pasando un string solo, luego un string con *, y luego un string con .split(). Explica la diferencia.


#🔵 Nivel 3 – Avanzado

#3.1  Crea una función filtrar_enteros(*args) que reciba datos mezclados y retorne solo los que sean int.

#3.2  Crea una función agregar_valor_final(*args) que convierta args en lista, agregue un elemento extra y lo retorne.

#3.3  Dada una lista de nombres, usa * para llamar a una función que los imprima numerados:
'''
nombres = ["Pepe","Juan","Loli","Sara"]
# Resultado esperado:
# 1. Pepe
# 2. Juan
# ...
'''

#3.4  Crea una función que acepte *args con palabras y genere un acrónimo (ej: "Python", "Software", "Foundation" → PSF).

#🧠 Reto final

#Escribe una función procesar(*args) que haga lo siguiente:
#Reciba un número indeterminado de argumentos
#Separe los que sean números y sume solo esos
#Una en un string los que sean cadenas
#Devuelva un diccionario con:
'''
{
    "suma_numeros": ...,
    "texto_unido": ...,
    "cantidad_argumentos": ...
}
'''



    
