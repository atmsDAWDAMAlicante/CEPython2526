# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 9 - ENUNCIADO: 
# Escribe una clase de Python llamada Círculo construida a partir de un radio y
# dos métodos que calcularán el área y el perímetro de un círculo.
# Prueba el ejercicio calculando el área y el perímetro de diferentes radios de círculos.

# Introduce el radio del círculo: 4
# Área del círculo: 50.27
# Perímetro del círculo: 25.13

import os
os.system("cls")

import math

# Modelo

class Circulo:
    def __init__ (self, radio):
        self.radio = radio
    
    def area(self):
        area = math.pi * (self.radio ** 2)
        return area
    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro


# Vista
def obtener_radio():
    while True:
        radio = input("Introduce el radio del círculo: ")
        try:
            radio = float(radio)
        except ValueError:
            print("Error: ¡Introduce un número!")
        else:
            return radio
        
def mostrar_circulo(circulo):
    print(f'Círculo con radio: {circulo.radio}')
    print(f'Área del círculo: {circulo.area():.2f}')
    print(f'Perímetro del círculo: {circulo.perimetro():.2f}')

# Controlador
def main():
    circulo1 = Circulo(obtener_radio())
    mostrar_circulo(circulo1)

if __name__ == "__main__":
    main()