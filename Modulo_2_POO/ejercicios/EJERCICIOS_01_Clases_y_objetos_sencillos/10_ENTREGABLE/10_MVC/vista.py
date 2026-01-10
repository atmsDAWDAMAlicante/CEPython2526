#from modelo import Validaciones



# Introducir opciones
class Introduccion():
    @staticmethod
    def introducir_operacion():
        operacion = input(f'Introduzca una operacion: ')
        #Validaciones.validar_enteros(operacion)
        return operacion
    

# Impresión por consola
class Impresion():
    @staticmethod
    def impresion_basica(texto):
        print(texto)