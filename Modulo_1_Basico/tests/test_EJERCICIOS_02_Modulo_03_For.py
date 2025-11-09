import pytest
import ejercicios.EJERCICIOS_02_Modulo_03_For as mod2_eje3

primeros_tres_ejercicios = "1  2  3  4  5  6  7  8  9  10 \n2  4  6  8  10 12 14 16 18 20 \n20 23 26 29 32 35 38 41 44 47 \n10 14 18 22 26 30 \n40 35 30 25 20 15 10 5  0  "

def test_ejercicio01():
    assert mod2_eje3.ejercicio_01() == primeros_tres_ejercicios

def test_ejercicio02():
    assert mod2_eje3.ejercicio_02() == primeros_tres_ejercicios

def test_ejercicio03():
    assert mod2_eje3.ejercicio_03() == primeros_tres_ejercicios


def test_ejercicio04():
    assert mod2_eje3.ejercicio_04(1) == "1  4  9  16 25 36 49 64 81 100"
    assert mod2_eje3.ejercicio_04(2) == "2  5  10 17 26 37 50 65 82 101"
    assert mod2_eje3.ejercicio_04(3) == "8  27 64 125 216 343"
    assert mod2_eje3.ejercicio_04(4) == "2  6  12 20 30 42 56"
    '''
    assert mod2_eje3.ejercicio_04(5) == "1  10 100 1000 10000"
    assert mod2_eje3.ejercicio_04(6) == "1.0 0.1 0.01 0.001 0.0001"
    assert mod2_eje3.ejercicio_04(7) == "1 -1 1 -1 1 -1 1 -1"
    '''

def test_ejercicio05():
    assert mod2_eje3.ejercicio_05(6,2) == "¡Te he pedido un número entero mayor que 6!"
    assert mod2_eje3.ejercicio_05(4,8) == "El número 4 es par\nEl número 5 es impar\nEl número 6 es par\nEl número 7 es impar\nEl número 8 es par\n"
    assert mod2_eje3.ejercicio_05(5,5) == "El número 5 es impar"


def test_ejercicio06():
    assert mod2_eje3.ejercicio_06(7,7) == "¡Te he pedido un número entero mayor que 7!"
    assert mod2_eje3.ejercicio_06(30,32) == "La suma desde 30 hasta 32 es 93\n30 + 31 + 32 = 93"


def test_ejercicio07():
    assert mod2_eje3.ejercicio_07(-5) == "¡Le he pedido un número entero mayor que cero!"
    assert mod2_eje3.ejercicio_07(5) == "El factorial de 5 es: 120"


'''
def test_ejercicio08():
    assert mod2_eje3.ejercicio_08(5) == 10

def test_ejercicio09():
    pass
    assert mod2_eje3.ejercicio_09(-5) == "¡Le he pedido un número entero mayor que cero!"pass
'''


def test_ejercicio10():
    assert mod2_eje3.ejercicio_10(-5) == "¡El número introducido debe ser un entero mayor de cero!"
    assert mod2_eje3.ejercicio_10(200) == "Los 12 divisores de 200 son 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 y 200."

def test_ejercicio11():
    assert mod2_eje3.ejercicio_11(-5) == "¡El número introducido debe ser un entero mayor de cero!"
    assert mod2_eje3.ejercicio_11(200) == "200 no es un número primo.\nLos 12 divisores de 200 son 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 y 200."
    assert mod2_eje3.ejercicio_11(7) == "7 es un número primo."

#Para la realización de la primera parte del ejercicio 12
'''
def test_ejercicio12():
    assert mod2_eje3.ejercicio_12(28) == "Divisores propios: [1, 2, 4, 7, 14]\nSuma de divisores: 28"
    assert mod2_eje3.ejercicio_12(12) == "Divisores propios: [1, 2, 3, 4, 6]\nSuma de divisores: 16"
    assert mod2_eje3.ejercicio_12(220) == "Divisores propios: [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]\nSuma de divisores: 284"
'''
#Para la realización del ejercicio 12 completo
def test_ejercicio12():
    assert mod2_eje3.ejercicio_12(28) == "Divisores propios: [1, 2, 4, 7, 14]\nSuma de divisores: 28\nEl número 28 es PERFECTO."
    assert mod2_eje3.ejercicio_12(12) == "Divisores propios: [1, 2, 3, 4, 6]\nSuma de divisores: 16\nEl número 12 es ABUNDANTE."
    assert mod2_eje3.ejercicio_12(220) == "Divisores propios: [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]\nSuma de divisores: 284\nEl número 220 es AMIGO del número 284."


