# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 1 - ENUNCIADO: Crea un programa. En el programa crea una clase, 
# a la que llamarás “libro”, que defina las característicasde los libros de tu biblioteca
# personal. La clase debe de tener dos propiedades:
# - propietario: El valor de esta propiedad ha de ser tu nombre completo.
# - read: Esta propiedad tomará inicialmente el valor lógico False e indicará 
# si un libro ha sidoya leído o todavía no.
# Crea un objeto tipo “libro” y muestra por pantalla el valor de sus dos propiedades.

class Libro:
    def __init__(self,propietario, read=False):
        self.propietario = propietario
        self.read = read



# Ejercicio 2 - ENUNCIADO: 



# Ejecución del programa
import os
os.system('cls')


# Vista
def mostrar_libro(libro):
    print(f'{libro.propietario} es propietario del libro. Ha sido leido: {libro.read}')

def main():
    Libro1 = Libro("Angel", True)
    mostrar_libro(Libro1)

main()

if __name__ == "main":
    main()