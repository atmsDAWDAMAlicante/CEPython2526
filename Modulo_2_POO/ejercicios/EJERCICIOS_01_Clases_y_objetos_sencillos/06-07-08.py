# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 6 - ENUNCIADO: Crea un nuevo programa. 
# Define en él de nuevo la clase “triángulo” con las mismas propiedades que 
# en los ejercicios anteriores:
    # - tipo: tomará el valor “Triángulo”
    # - lados: asígnale el valor 3
    # - base: asígnale el valor 0
    # - altura: asígnale el valor 0

# Crea un objeto triangulo y asígnale el valor 5 a la longitud de la base y 
# 4 a la longitud de la altura. 
# Crea un segundo objeto triángulo. El programa debe preguntar al usuario por 
# la longitud de la base y de la altura de este segundo triángulo. 
# Establece estos valores como estado de las propiedades base y altura 
# del segundo triángulo.
# 
# Muestra las propiedades de los dos triángulos por pantalla.

'''
---- Datos segundo triángulo ----
Introduce la longitud de la base: 5.4
Introduce la longitud de la altura: 3.27
-------- Propiedades del primer triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 5
Altura: 4
-------- Propiedades del segundo triángulo--------
Número de lados: 3
Tipo de polígono: Triángulo
Base: 5.4
Altura: 3.27
'''



# Ejercicio 7 - ENUNCIADO: Partimos del ejercicio anterior. 
# Vamos añadir un método a la clase triangulo. Este método ha de calcular 
# la superficie del triángulo. Ten en cuenta que tendrás que utilizar 
# las propiedades base y altura de cada objeto para calcular dentro del
# método el valor de la superficie. Una vez creado el método que calcula 
# la superficie de los objetos de la clase triangulo. Añade el código 
# necesario para que se muestre la superficie de los dos triángulos. 
# Este valor se tiene que obtener llamando al método creado en 
# la primera parte del ejercicio.

# Consejo: Para referirte a una propiedad del objeto dentro del método 
# tendrás que utilizar el parámetro self. Por ejemplo, para referirte 
# a la base tendrás que utilizar la sintaxis self.base.

'''
---- Datos segundo triángulo ----
Introduce la longitud de la base: 5.4
Introduce la longitud de la altura: 3.27
-------- Propiedades del primer triángulo--------
Base: 5
Altura: 4
El area es: 10.00
-------- Propiedades del segundo triángulo--------
Base: 5.4
Altura: 3.27
El area es: 8.83
'''





# Ejercicio 8 - ENUNCIADO: Modifica el código anterior para que el programa 
# nos informe de cuál de los dos triángulos tiene una superficie mayor:


'''
---- Datos segundo triángulo ----
Introduce la longitud de la base: 5
Introduce la longitud de la altura: 8
-------- Propiedades del primer triángulo--------
Base: 5
Altura: 4
El área del primer triángulo es: 10.00
-------- Propiedades del segundo triángulo--------
Base: 5.0
Altura: 8.0
El área del segundo triángulo es: 20.00
El segundo triángulo tiene una superficie mayor que el primero.
'''

'''
---- Datos segundo triángulo ----
Introduce la longitud de la base: 2
Introduce la longitud de la altura: 10
-------- Propiedades del primer triángulo--------
Base: 5
Altura: 4
El área del primer triángulo es: 10.00
-------- Propiedades del segundo triángulo--------
Base: 2.0
Altura: 10.0
El área del segundo triángulo es: 10.00
Los dos triángulos tienen la misma superficie.

'''