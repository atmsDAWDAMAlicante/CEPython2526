import pytest
#from ejercicios.EJERCICIOS_01_Modulo_01 import *
import ejercicios.EJERCICIOS_01_Modulo_01 as mod1_eje1


def test_ejercicio_01():
    assert mod1_eje1.ejercicio_01("Angel") == "Encantado de conocerte, Angel."

def test_ejercicio_02():
    assert mod1_eje1.ejercicio_02(50.00) == 13.89

def test_ejercicio_03():
    assert mod1_eje1.ejercicio_03(1000.00,2.00) == 20.00

def test_ejercicio_04():
    assert mod1_eje1.ejercicio_04(1,9,6) == (-0.7250827823646251, -8.274917217635375)

def test_ejercicio_05():
    assert mod1_eje1.ejercicio_05(40.00) == (104.00, 313.00)

def test_ejercicio_06():
    assert mod1_eje1.ejercicio_06(20.00) == (1.33, 1.03, 0.83, 17.00, 21.8, 350.45)

def test_ejercicio_07():
    assert mod1_eje1.ejercicio_07(40.00) == (1600.00, 692.82)

def test_ejercicio_08():
    assert mod1_eje1.ejercicio_08(90,1.79) == (28.09)

def test_ejercicio_09():
    assert mod1_eje1.ejercicio_09(15,4) == (3,3)

def test_ejercicio_10():
    assert mod1_eje1.ejercicio_10() == 0.25