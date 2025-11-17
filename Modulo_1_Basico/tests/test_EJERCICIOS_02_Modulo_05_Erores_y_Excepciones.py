import pytest
import ejercicios.EJERCICIOS_02_Modulo_05_Errores_y_Excepciones as mod2_eje5

def test_ejercicio01():
    assert mod2_eje5.ejercicio_01(10,5) == 2
    assert mod2_eje5.ejercicio_01(10,0) == "No es posible dividir entre cero, debes introducir un número distinto."

def test_ejercicio02():
    assert mod2_eje5.ejercicio_02(3) == "pato"
    assert mod2_eje5.ejercicio_02(5) == "El índice se encuentra fuera del rango.\nDebes utilizar un número mayor o igual que cero y menor que la longitud de la lista."

def test_ejercicio03():
    assert mod2_eje5.ejercicio_03("azul") == "azul en inglés se dice blue"
    assert mod2_eje5.ejercicio_03("amarillo") == "Error: El término amarillo no se encuentra en este diccionario, debes probar con otro que sí exista."

def test_ejercicio04():
    assert mod2_eje5.ejercicio_04(5,4) == "5 + 4 = 9"
    assert mod2_eje5.ejercicio_04(3,2.5) == "El valor introducido no es un número entero"
    assert mod2_eje5.ejercicio_04(3,"Hola") == "El valor introducido no es un número entero"

def test_ejercicio05():
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], 10) == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: 10\nLa lista actual es: [1, 'pie', -2, 10]"
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], 'pie') == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: pie\nError: Imposible añadir elementos duplicados => pie\nLa lista actual es: [1, 'pie', -2]"
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], "Hola") == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: Hola\nLa lista actual es: [1, 'pie', -2, 'Hola']"

'''
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], 10) == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: 10\nLa lista actual es: [1, 'pie', -2, 10]"
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], 'pie') == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: pie\nError: Imposible añadir elementos duplicados => pie\nLa lista actual es: [1, 'pie', -2, '10']"
    assert mod2_eje5.agregar_una_vez([1, 'pie', -2], "Hola") == "La lista actual es: [1, 'pie', -2]\nValor que quieres añadir a la lista: Hola\nLa lista actual es: [1, 'pie', -2, '10', 'Hola']"
'''


def test_ejercicio06():
    pass

def test_ejercicio07():
    pass


def test_ejercicio08():
    pass
