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


print(f"---Ejercicio nº 11: Declaración de la renta IRPF")

from decimal import Decimal #para operar con moneda en la variable renta o base 

resultado = ""

def calculo_IRPF(nombre, edad, ingresos):
    resultado = ""
    edad = int(edad)
    ingresos = Decimal(ingresos)
    impuestos_brutos = [Decimal(0),0]
    impuestos_netos = Decimal(0)
    descuento_edad = Decimal(0)
    descuento_adicional = Decimal(0)
    descuento_mensaje = ""

    if (edad < 18):
        resultado = "No paga impuestos"
    else:
        # Este supuesto evalúa el resto de edades
        # Lo primero es obtener los impuestos brutos (antes de los descuentos)
        # Para ello se llama a la función que devolverá la cantidad de impuestos brutos 
        # en función de los ingresos, que se pasan por parámetro
        impuestos_brutos = calcular_Impuestos(ingresos)

        # 2º Con el impuesto bruto se procede al cálculo de los descuentos
        # 2.1  Cálculo del descuento por edad
        descuento_edad = descuento_anyos(edad, impuestos_brutos[0])
        # Se muestra el descuento de la edad en el mensaje en la consola
        if (descuento_edad > 0):
            descuento_mensaje += f"Descuento de edad por importe: {descuento_edad:.2f} €\n"
       
        # 2.2 - Cálculo del descuento adicional
        descuento_adicional = descuento_nombre(nombre, impuestos_brutos[0])
        # Se muestra el descuento de la letra del nombre en el mensaje en la consola
        if (descuento_adicional > 0):
            descuento_mensaje += f"Descuento adicional por importe: {descuento_adicional:.2f} €\n"

        # 3 - Cálculo de los impuestos netos
        impuestos_netos = impuestos_brutos[0] - (descuento_edad + descuento_adicional)

        resultado = f'El impuesto bruto: {impuestos_brutos[0]:.2f} €\n' \
        f'{descuento_mensaje}' \
        f'El impuesto final a pagar {impuestos_netos:.2f} €\n' \
        f'A {nombre}, con {edad} años, se le ha aplicado un {(impuestos_brutos[1])*100:.2f}%\n' \
        f'ya que ingresa {ingresos:.2f} €.'

    return resultado

def calcular_Impuestos(ingresos): #Esta función calcula los impuestos brutos (antes de los descuentos)

    # Se convierte en Decimal todo para poder operar
    tipo = Decimal(0)
    calculo = Decimal(0)
    if (ingresos < Decimal(15000)):
        tipo = Decimal(0.05)
    elif (ingresos >= Decimal(15000)) and (ingresos < Decimal(30000)):
        tipo = Decimal(0.1)
    elif (ingresos >= Decimal(30000)) and (ingresos < Decimal(60000)):
        tipo = Decimal(0.2)
    else:
        tipo = Decimal(0.3)
    calculo = ingresos * tipo
    return [calculo,tipo] # retorna el impuesto bruto y el tipo (para mostrarlo en el mensaje final)

# Funcion para calcular el descuento para mayores de 65 años
def descuento_anyos(edad, importe_impuestos_brutos):
    if (edad > 65):
        descuento_edad = importe_impuestos_brutos * Decimal(0.5)
        return descuento_edad
    else:
        return 0

# Función para calcular el descuento de quienes tienen un nombre que empieza por a o A
def descuento_nombre(nombre, importe_impuestos_brutos):
    nombre = nombre.upper()
    if (nombre[0] == "A"):
        descuento_nombre = importe_impuestos_brutos * Decimal(0.02)
        return descuento_nombre
    else:
        return 0

#INPUTS para probar el programa
nombre = input("Introduce el nombre del contribuyente: ")
edad = int(input("Introduce la edad del contribuyente: "))
renta = Decimal(input("Introduce la renta del contribuyente: "))
resultado = calculo_IRPF(nombre, edad, renta)
print(resultado)


#Lineas comentadas con llamadas a la función principal para probar el programa más rápidamente
'''
linea = "-------------------------"
print(linea)
print(calculo_IRPF("Angel",66, 80000))
print(linea)
print(calculo_IRPF("Paquito",13, 3))
print(linea)
print(calculo_IRPF("Manolo", 33, 30000))
print(linea)
print(calculo_IRPF("Lola", 80, 5000))
print(linea)
print(calculo_IRPF("Ataulfo", 33, 54000))
'''
















'''
Código del test con pytest:
def test_entregable_11():
    assert entregable_ejer_011.ejercicio_011(1,-2,2) == "Sin solución real"


'''