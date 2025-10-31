import pytest
import ejercicios.EJERCICIOS_02_Modulo_01_Condicionales as mod2_eje1

def test_ejercicio01():
    #Hay que recordar que en el ejercicio se convierten en float los parámetros
    assert mod2_eje1.ejercicio_01(14,5) == "La división no es exacta. Cociente: 2.0 Resto: 4.0"
    assert mod2_eje1.ejercicio_01(20,4) == "La división es exacta. Cociente: 5.0"
    assert mod2_eje1.ejercicio_01(20,0) == "No se puede dividir por 0"
def test_ejercicio02():
    assert mod2_eje1.ejercicio_02(23,14.5) == "Menor: 14.5; Mayor: 23.0"
    assert mod2_eje1.ejercicio_02(5.0,5) == "Los dos números son iguales"

def test_ejercicio03():
    assert mod2_eje1.ejercicio_03(1970,2025) == "Faltan 55 años para llegar"
    assert mod2_eje1.ejercicio_03(2025,1970) == "Han pasado 55 años"
    assert mod2_eje1.ejercicio_03(1970,1971) == "Falta 1 año para llegar"
    assert mod2_eje1.ejercicio_03(1971,1970) == "Ha pasado 1 año"


def test_ejercicio04():
    pass

def test_ejercicio05():
    pass


def test_ejercicio06():
    pass

def test_ejercicio07():
    pass


def test_ejercicio08():
    assert mod2_eje1.ejercicio_08(1,-2,2) == "Sin solución real"
    assert mod2_eje1.ejercicio_08(0,0,5) == "Sin solución"
    assert mod2_eje1.ejercicio_08(0,0,0) == "Todos los números son solución"
    assert mod2_eje1.ejercicio_08(2,-7,3) == "Las soluciones de la ecuación son 3.0 y 0.5"
    assert mod2_eje1.ejercicio_08(1,2,1) == "Las soluciones de la ecuación son -1.0 y -1.0"
def test_ejercicio09():
    pass


def test_ejercicio10():
    pass

def test_ejercicio11():
    pass





