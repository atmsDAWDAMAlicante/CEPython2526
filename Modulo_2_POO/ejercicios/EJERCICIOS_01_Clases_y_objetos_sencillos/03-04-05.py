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

# Funcion que devuelve el string número ordinal para identificar el triángulo
def obtener_ordinal(lista_triangulos, tri):
    if (lista_triangulos.index(tri) == 0): #OJO, el primer índice es 0
        return "primer"
    elif (lista_triangulos.index(tri) == 1):
        return "segundo"
    elif (lista_triangulos.index(tri) == 2):
        return "tercero"
    else: # A partir del tercero se le pone un º y no se redacta
        return f"{len(lista_triangulos)}º"

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
def mostrar_triangulo(triangulo, ordinal):
    print(f'-------- Propiedades del {ordinal} triángulo--------')
    print(f'Número de lados: {triangulo.lados}')
    print(f'Tipo de polígono: {triangulo.tipo}')
    print(f'Base: {triangulo.base}')
    print(f'Altura: {triangulo.altura}')

# Controlador

# Función que obtiene el ordinal de cada triángulo y llama a la vista para su impresión

datos_actualizados = "*************** DATOS ACTUALIZADOS ******************"

def impresion_triangulos(lista_triangulos):
    for triangulo in lista_triangulos:
      #print(triangulo)
      ordinal = obtener_ordinal(lista_triangulos, triangulo)
      mostrar_triangulo(triangulo,ordinal)

def main():
    lista_triangulos = [] # Lista que recoge los objetos triángulo
    # Se crea el primer objeto
    triangulo1 = Triangulo(3,0,0)
    lista_triangulos.append(triangulo1) # Se añade a la lista
    triangulo2 = Triangulo(3,0,1)
    lista_triangulos.append(triangulo2)
    impresion_triangulos(lista_triangulos)
    
    # Modificación de los valores del primer triángulo
    triangulo1.base = 5
    #lista_triangulos[0].base = 5
    triangulo1.altura = 4
    #lista_triangulos[0].altura = 4
    print(datos_actualizados)
    impresion_triangulos(lista_triangulos)






if __name__ == "__main__":
    main()