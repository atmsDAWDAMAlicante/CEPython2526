import pytest
import ejercicios.EJERCICIOS_02_Modulo_01_Condicionales as mod2_eje1
#import ejercicios.EJ_ENTREGABLES_02_Modulo_01_Condicionales.ejer_08 as entregable_ejer_08
#import ejercicios.EJ_ENTREGABLES_02_Modulo_01_Condicionales.ejer_09 as entregable_ejer_09
#import ejercicios.EJ_ENTREGABLES_02_Modulo_01_Condicionales.ejer_11 as entregable_ejer_11

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
    #assert mod2_eje1.ejercicio_08(2,-7,3) == "Las soluciones de la ecuación son 3.0 y 0.5"
    assert mod2_eje1.ejercicio_08(1,2,1) == "Las soluciones de la ecuación son -1.0 y -1.0"
    
    
def test_ejercicio09():
    pass


def test_ejercicio10():
    pass

def test_ejercicio11():
    pass

def test_entregable_08():
    pass
    '''
    assert entregable_ejer_08.ejercicio_08(1,-2,2) == "Sin solución real"
    assert entregable_ejer_08.ejercicio_08(0,0,5) == "Sin solución"
    assert entregable_ejer_08.ejercicio_08(0,0,0) == "Todos los números son solución"
    assert entregable_ejer_08.ejercicio_08(2,-7,3) == "Las soluciones de la ecuación son 3.0 y 0.5"
    assert entregable_ejer_08.ejercicio_08(1,2,1) == "Una solución: -1.00"
    #assert entregable_ejer_08.ejercicio_08(0,3,2) == "¿DIVISÓN POR CERO?"
    '''


def test_entregable_09():
    '''
    #assert entregable_ejer_09.figura_Area("lñjñL") == "Entrada no válida"
    assert entregable_ejer_09.circulo(2.0) == "Un círculo de radio 2.0 tiene un área de 12.566370614359172"
    assert entregable_ejer_09.triangulo(3,5.5) == "Un triángulo de base 3.0 y altura 5.5 tiene un área de 8.25"
    '''

def test_entregable_11():
    pass



