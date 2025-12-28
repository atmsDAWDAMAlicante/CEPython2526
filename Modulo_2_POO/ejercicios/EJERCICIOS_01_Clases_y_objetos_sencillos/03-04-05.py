# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 3 - ENUNCIADO: 
# Crea un programa. En el programa crea una clase, a la que llamarás “triangulo”. 
# La clase debe de tener cuatro propiedades:
    # - tipo: tomará el valor “Triángulo”
    # - lados: asígnale el valor 3
    # - base: asígnale el valor 0
    # - altura: asígnale el valor 0
# Crea un objeto tipo “triangulo” y muestra por pantalla el valor de sus 
# cuatro propiedades.
# POO – Creando clases y objetos sencillos
'''
3
Triángulo
0
0
'''

# Modelo
class Triangulo:
    def __init__(self, lados, base, altura):
        self.tipo = "Triángulo"
        self.lados = lados
        self.base = base
        self.altura = altura


def obtener_ordinal(lista):
    if (len(lista) == 1):
        return "primero"
    elif (len(lista) == 2):
        return "segundo"
    elif (len(lista) == 3):
        return "tercero"
    else:
        return f"{len(lista)}º"

# Ejercicio 4 - ENUNCIADO: Partiendo del programa anterior crea un segundo 
# objeto triángulo y muestra las propiedadesde los dos objetos por pantalla. 
# Enriquece un poco el formato de las órdenes print para mostrar 
# de manera más clara la información.
'''
-------- Propiedades del primer triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 0
Altura: 0
-------- Propiedades del segundo triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 0
Altura: 0
'''


# Ejercicio 5 - ENUNCIADO: Partimos de nuevo del ejercicio anterior. 
# Una vez que has mostrado los datos de los dos triángulos modifica los 
# valores de la base y la altura del primer triángulo (no en la clase triángulo, 
# debes cambiarlos en el objeto). Los nuevos valores para el primer 
# objeto serán:
    # - base = 5
    # - altura = 4
# Muestra de nuevo las propiedades de los dos objetos.


'''
-------- Propiedades del primer triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 0
Altura: 0
-------- Propiedades del segundo triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 0
Altura: 0
*************** DATOS ACTUALIZADOS ******************
-------- Propiedades del primer triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 5
Altura: 4
-------- Propiedades del segundo triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 0
Altura: 0
'''




# Ejecución del programa
import os
os.system('cls')


# Vista
def mostrar_triangulo(triangulo,ordinal):
    print(f'-------- Propiedades del {ordinal} triángulo--------')
    print(f'Número de lados: {triangulo.lados}')
    print(f'Tipo de polígono:{triangulo.tipo}')
    print(f'Base:{triangulo.base}')
    print(f'Altura: {triangulo.altura}')

# Controlador
def main():
    lista_triangulos = []
    triangulo1 = Triangulo(3,0,0)
    lista_triangulos.append(triangulo1)
    ordinal = obtener_ordinal(lista_triangulos)
    mostrar_triangulo(triangulo1,ordinal)

    triangulo2 = Triangulo(3,0,0)
    lista_triangulos.append(triangulo2)
    ordinal = obtener_ordinal(lista_triangulos)
    mostrar_triangulo(triangulo2,ordinal)

datos_actualizados = "*************** DATOS ACTUALIZADOS ******************"

if __name__ == "__main__":
    main()