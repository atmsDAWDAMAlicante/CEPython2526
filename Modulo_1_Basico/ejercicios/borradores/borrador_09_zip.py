#Ejercicios sugeridos por el Chat GPT


'''
¡Perfecto! Aquí tienes una serie de ejercicios progresivos para practicar zip + diccionarios. Intenta resolverlos tú y luego, si quieres, te paso las soluciones para comparar.

🟩 Nivel 1 – básicos

Crea dos listas del mismo tamaño (nombres y edades) y genera un diccionario del tipo:
{"Ana": 20, "Luis": 22, ...} utilizando zip.

A partir del ejercicio anterior, imprime la edad de un nombre concreto usando get().

Usa zip para unir dos tuplas con países y capitales y convertirlas en diccionario.

¿Qué ocurre si zipeas listas de distinta longitud?
Haz la prueba y explica tu observación.

🟨 Nivel 2 – manipulación

Dadas dos listas, crea un diccionario y luego obtén solo las claves y solo los valores en listas.

Convierte un diccionario en dos listas independientes usando zip al revés:

claves, valores = zip(*mi_diccionario.items())


Comprobar que claves y valores contienen lo esperado.

Crea dos listas de asignaturas y notas.
Genera el diccionario y después calcula la nota media.

🟥 Nivel 3 – retos

Tienes estas listas:

productos = ["pan", "leche", "huevos", "café"]
precios = [1.10, 0.95, 2.50, 3.20]


Crea un diccionario producto:precio.

Muestra los productos con precio mayor a 2 euros.

Calcula el total de compra si compras uno de cada uno.

Une tres listas con zip (por ejemplo: nombre, edad, ciudad) y conviértelas en lista de diccionarios así:

[
    {"nombre": "Ana", "edad": 20, "ciudad": "Madrid"},
    ...
]


Usa zip para mezclar dos diccionarios por clave y generar uno nuevo con el formato:

clave : (valor1, valor2)


Ejemplo:

d1 = {"a":1, "b":2, "c":3}
d2 = {"a":10,"b":20,"c":30}
→ {"a":(1,10),"b":(2,20),"c":(3,30)}

🏆 Nivel experto (si te animas)

Tienes listas de alumnos y 3 notas por alumno:

alumnos = ["Ana","Pepe","Lola"]
n1 = [7,5,9]
n2 = [8,6,7]
n3 = [9,10,8]


📌 Crea un diccionario así:

{
    "Ana": {"nota1":7, "nota2":8, "nota3":9, "media": 8.0},
    ...
}

Si quieres, cuando termines envíame tu código y te lo reviso, como la vez anterior 😄

¿Quieres que más tarde te prepare un mini test/práctica final con corrección automática?
'''


