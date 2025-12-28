# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 1 - ENUNCIADO: Crea un programa. En el programa crea una clase, 
# a la que llamarás “libro”, que defina las característicasde los libros de tu biblioteca
# personal. La clase debe de tener dos propiedades:
# - propietario: El valor de esta propiedad ha de ser tu nombre completo.
# - read: Esta propiedad tomará inicialmente el valor lógico False e indicará 
# si un libro ha sidoya leído o todavía no.
# Crea un objeto tipo “libro” y muestra por pantalla el valor de sus dos propiedades.
'''
class Libro:
    def __init__(self,propietario, read=False):
        self.propietario = propietario
        self.read = read
'''


# Ejercicio 2 - ENUNCIADO: Partiendo del programa anterior añade a la clase “libro” 
# dos métodos:
    # - El primer método informará de si un libro ha sido ya leído o todavía no. 
    # Para ello ha de mostrar: uno de los dos mensajes siguientes:
      # o Si la propiedad read tiene el valor False: “Todavía no has leído este libro”.
      # o Si la propiedad read tiene el valor True: “Ya has leído este libro”.
    # - El segundo método realizará la acción de cambiar el valor de la propiedad 
    # read de False a True.

# A continuación, el programa realizará las siguientes opciones:
    # - Crea un objeto “libro”.
    # - Muestra por pantalla el estado de las propiedades propietario y read 
    #   al iniciar la ejecución del programa.
    # - Ejecuta el método que informa sobre si hemos leído el libro o no.
    # - Ejecuta el método que cambia el valor de la propiedad read a True
    # - Muestra de nuevo las propiedades el objeto que acabas de crear.
    # - Ejecuta el método que informa sobre si hemos leído el libro o no.



# Ejecución del programa
import os
os.system('cls')

# Modelo
class Libro:
    def __init__ (self, propietario, read = False):
        self.propietario = propietario
        self.read = read

    def ha_sido_leido(self):
        if self.read == False:
            print("Todavía no has leído este libro.")
        else:
            print("Ya has leído este libro.")

    def cambiar_estado_libro(self):
        self.read = not self.read

# Vista
def mostrar_libro(libro):
    print(f'{libro.propietario} es propietario del libro. Ha sido leido: {libro.read}')

# Controlador
def main():
    libro1 = Libro("Andrés Sánchez", False)
    mostrar_libro(libro1)
    libro1.ha_sido_leido()
    libro1.cambiar_estado_libro()
    mostrar_libro(libro1)
    libro1.ha_sido_leido()

main()

if __name__ == "main":
    main()