import pytest
import ejercicios.EJERCICIOS_02_Modulo_01_Condicionales as mod2_eje1


def test_ejercicio_01():
    assert mod2_eje1.ejercicio_01("Angel") == ["ANGEL", "angel", "Angel"]

def test_ejercicio_02():
    assert mod2_eje1.ejercicio_02("+34-913724710-56") == "913724710"

def test_ejercicio_03():
    assert mod2_eje1.ejercicio_03("09/07/70") == "09 de Julio de 70"


def test_ejercicio_04():
    assert mod2_eje1.ejercicio_04("09/07/1970",1) == "09 de July de 1970"

def test_ejercicio_05():
    assert mod2_eje1.ejercicio_05("VaCaCiOnEs") == "Acceso permitido"
    assert mod2_eje1.ejercicio_05("examenes") == "Acceso denegado"

def test_ejercicio_06():
    pass