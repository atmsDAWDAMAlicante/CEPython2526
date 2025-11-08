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
    assert mod2_eje3.ejercicio_04() == "1  4  9  16 25 36 49 64 81 100\n2  5  10 17 26 37 50 65 82 101\n8  27 64 125 216 343\n2  6  12 20 30 42 56\n1  10 100 1000 10000\n1.0 0.1 0.01 0.001 0.0001\n1 -1 1 -1 1 -1 1 -1"


def test_ejercicio05():
    assert mod2_eje3.ejercicio_05(6,2) == "¡Te he pedido un número entero mayor que 6!"
    assert mod2_eje3.ejercicio_05(4,8) == "El número 4 es par\nEl número 5 es impar\nEl número 6 es par\nEl número 7 es impar\nEl número 8 es par\n"
    assert mod2_eje3.ejercicio_05(5,5) == "El número 5 es impar"

'''
def test_ejercicio06():
    assert mod2_eje3.ejercicio_05(7,7) == "¡Te he pedido un número entero mayor que 7!"
    assert mod2_eje3.ejercicio_05(30,32) == "La suma desde 30 hasta 32 es 93\n30 + 31 + 32 = 93"


def test_ejercicio07():
    pass


def test_ejercicio08():
    assert mod2_eje3.ejercicio_08(5) == 10

def test_ejercicio09():
    pass
'''

def test_ejercicio10():
    pass



