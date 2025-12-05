import pytest
import ejercicios.EJERCICIOS_03_Modulo_01 as mod1_eje3

def test_ejercicio09():
    assert mod1_eje3.ejercicio09() == "Buenos días\nBuenos días\n"

def test_ejercicio10():
    #pass
    assert mod1_eje3.ejercicio10(2,5,7) == 7507