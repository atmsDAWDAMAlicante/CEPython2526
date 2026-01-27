#EJERCICIOS ENTREGABLES MÓDULO 2 - POO
#UNIDAD 1 - Introducción a la POO en Python
#Ejercicio nº 10
# ALUMNO: XX

import os
import decimal # se importa para el cálculo de las nóminas
from modelo import Empleado, empresa, Validaciones
from vista import Introduccion, Impresion

os.system('cls')

# Variables globales-títulos generales
mensaje_inicio_programa = "=== Inicio del programa ==="
mensaje_fin_programa = "=== Fin del programa ==="

# Menú principal del programa
menu_inicial = "1.- Cambiar departamento\n2.- Calculo nómina/horas extra\n3.- Info empleado\n4.- Info completa\n\n0.- Salir: ---> "

def main(): # Inicio del programa: menú principal
    Impresion.impresion_basica(mensaje_inicio_programa)
    
    while True: # Menú principal del programa
        Impresion.impresion_basica("Seleccione una opción:")
        num = Introduccion.introducir_operacion(menu_inicial) # Llama a la Vista
        # Las validaciones se hacen en el Modelo
        operacion = Validaciones.validar_enteros(num)
        operacion = Validaciones.validar_rango(operacion, 4)

        # Bifurcación de opciones del menú principal
        if (operacion != -1):
            if (operacion == 1): # La función llamada contiene un submenú para elegir empleado
                Impresion.impresion_basica("\nCambiar de departamento. Seleccione: ")
                cambiar_departamento()
            elif (operacion == 2):
                calcular_salario()
            elif (operacion == 3): # La función llamada contiene un submenú para elegir empleado
                Impresion.impresion_basica("\nSeleccione el empleado/jefazo: ")
                mostrar_info_individual()
            elif (operacion == 4):
                Impresion.mostrar_info_toda_la_empresa(empresa)
            elif (operacion == 0):
                Impresion.impresion_basica(mensaje_fin_programa)
                break
            else:
                continue


# MENÚS

def formar_menu_empleados_rasos(): # No incluye al que pertenece a "JEFAZOS"
    menu_lista = ""
    menu = ""
    lista_empleados = []
    for empleado in empresa:
        if (empleado.departamento != "JEFAZOS"): # En este condicional se elude a los "JEFAZOS"
            lista_empleados.append(empleado.nombre)
    menu_lista = list(enumerate(lista_empleados,start = 1))
    for num,elem in menu_lista:
        menu += f'{num} - {elem}\n'
    total = len(menu_lista)
    return menu, total, menu_lista

def formar_menu_plantilla(): # Función que forma un menú con todos los integrantes de la plantilla
    menu_lista = ""
    menu = ""
    lista_empleados = []
    for empleado in empresa:
        lista_empleados.append(empleado.nombre)
    menu_lista = list(enumerate(lista_empleados,start = 1))
    for num,elem in menu_lista:
        menu += f'{num} - {elem}\n'
    total = len(menu_lista)
    return menu, total, menu_lista


# OPERACIONES ESPECÍFICAS DE LA CLASE

# OPERACIÓN PARA CAMBIAR DE DEPARTAMENTO

def cambiar_departamento():
    menu, lim, listado = formar_menu_empleados_rasos()
    empleado = ""
    # Se selecciona el empleado excepto los "JEFAZOS"
    num = Introduccion.introducir_operacion(menu) # Vista
    # Validaciones en el Modelo
    operacion = Validaciones.validar_enteros(num)
    operacion = Validaciones.validar_rango(operacion,lim)
    if (operacion == -1):
        cambiar_departamento()
    else:
        # Aquí se introduce el nuevo departamento
        nuevo_departamento = Introduccion.introducir_operacion("Introduce el nuevo departamento: ")
        for num, elem in listado:
            if (num == operacion):
                empleado = elem
        for para_cambiar in empresa:
            if (para_cambiar.nombre == empleado):
                # AQUÍ SE LLAMA A LA FUNCIÓN DE CADA OBJETO modificar_departamento()
                para_cambiar.modificar_departamento(nuevo_departamento)
        Impresion.impresion_departamentos(empresa)

# OPERACIÓN PARA CALCULAR EL SALARIO EN FUNCIÓN DE LAS HORAS EXTRA

def calcular_salario():
    plantilla = []
    for empleado in empresa: # Se piden las horas extras de todos menos de los "JEFAZOS"
        elemento = [] # La info de cada empleado se agrupa en una lista "elemento"
        if (empleado.departamento != "JEFAZOS"): # Se eluden los "JEFAZOS" de la petición de horas
            elemento.append(empleado.nombre)
            horas = Introduccion.introducir_operacion(f'¿Cuántas horas ha hecho {empleado.nombre}? --> ') # Vista
            # Validaciones en el Modelo
            horas_num = Validaciones.validar_enteros(horas)
            if (horas_num == -1):
                calcular_salario()
            else:
                elemento.append(horas_num)
                # AQUÍ SE LLAMA A LA FUNCIÓN DE CADA OBJETO calcular_salario(se le pasan las horas)
                elemento.append(empleado.calcular_salario(horas_num))
                
        else:
            elemento.append(empleado.nombre)
            elemento.append(0)
            elemento.append(empleado.sueldo)
        # CADA lista elemento (cada empleado) se va agrupando en otra lista superior llamada "plantilla"
        plantilla.append(elemento) # Se va formando una lista con TODOS, incluido el "JEFAZO" con 0 horas extra
    
    Impresion.mostrar_nomina_mes(plantilla) # La lista plantilla es la que se envía a imprimir a la Vista

# OPERACIÓN PARA MOSTRAR LA INFORMACIÓN INDIVIDUAL DE CADA OBJETO (empleado)

def mostrar_info_individual():
    menu, lim, listado = formar_menu_plantilla() # Se muestran todos los empleados para elegir
    empleado = ""
    individuo = Introduccion.introducir_operacion(menu) # Vista
    # Validaciones en el Modelo
    operacion = Validaciones.validar_enteros(individuo)
    operacion = Validaciones.validar_rango(operacion,lim)
    if (operacion == -1):
        mostrar_info_individual()
    else:
        for individuo in listado:
            if (individuo[0] == operacion):
                empleado = individuo[1]
                
        for para_mostrar in empresa:
            if (para_mostrar.nombre == empleado):
                Impresion.impresion_basica(f"\n== IMPRIMIENDO INFORME de {para_mostrar.nombre} ...")
                # AQUÍ SE LLAMA A LA FUNCIÓN DE CADA OBJETO imprimir_info() del empleado seleccionado
                para_mostrar.imprimir_info()
                Impresion.impresion_basica(f"== INFORME de {para_mostrar.nombre} COMPLETADO.\n")

if __name__ == "__main__":
    main()


