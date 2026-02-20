# A) CLASE PADRE PRODUCTO Y CLASES HIJAS BEBIDA Y COMIDA

class Producto: # CLASE PADRE DE BEBIDA Y COMIDA
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def informacion(self):
        pass