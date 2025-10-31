#EJERCICIOS NTREGABLES UD 02 - Modulo 01 - Condicionales
#Ejercicio nº 11 
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

# Enunciado:
'''
Realiza un programa que pida:
    • El nombre del usuario
    • Su edad
    • Su ingreso anual (€)
El programa debe aplicar las siguientes reglas:
    1. Si la edad es menor de 18 → no paga impuestos.
    2. Si tiene entre 18 y 65 años:
        o Si gana menos de 15.000 €, paga un 5 % de impuestos.
        o Entre 15.000 € y 30.000 €, paga un 10 %.
        o Entre 30.000 € y 60.000 €, paga un 20 %.
        o Más de 60.000 €, paga un 30 %.
    3. Si tiene más de 65 años, se le aplica un descuento del 50 % sobre el impuesto
    correspondiente.
    4. Si su nombre empieza por “A” o “a”, obtiene un bono adicional de -2 % (descuento).
    5. El programa mostrará:
        El impuesto base aplicado
        El descuento (si procede)
        El impuesto final a pagar
        Un mensaje personalizado con su nombre y edad.
'''





















'''
Código del test con pytest:
def test_entregable_11():
    assert entregable_ejer_011.ejercicio_011(1,-2,2) == "Sin solución real"


'''