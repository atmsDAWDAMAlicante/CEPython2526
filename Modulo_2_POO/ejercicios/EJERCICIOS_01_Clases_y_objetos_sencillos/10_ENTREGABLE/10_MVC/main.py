import os
import decimal
from modelo import Empleado, empresa, Validaciones
from vista import Introduccion, Impresion

os.system('cls')

mensaje_inicio_programa = "=== Inicio del programa ==="
mensaje_fin_programa = "=== Fin del programa ==="

menu_inicial = "1.- Cambiar departamento\n2.- Calculo nómina/horas extra\n3.- Info empleado\n4.- Info completa\n\n0.- Salir: ---> "

def main(): # Inicio del programa: menú principal
    Impresion.impresion_basica(mensaje_inicio_programa)
    
    while True:
        Impresion.impresion_basica("Seleccione una opción:")
        num = Introduccion.introducir_operacion(menu_inicial)
        operacion = Validaciones.validar_enteros(num)
        operacion = Validaciones.validar_rango(operacion, 4)
        if (operacion != -1):
            if (operacion == 1):
                Impresion.impresion_basica("Cambiar de departamento. Seleccione: ")
                cambiar_departamento()
            elif (operacion == 2):
                calcular_salario()
            elif (operacion == 3):
                Impresion.impresion_basica("Seleccione el empleado/jefazo: ")
                mostrar_info_individual()
                Impresion.impresion_basica("== Informe completado\n")
            elif (operacion == 4):
                Impresion.mostrar_info_toda_la_empresa(empresa)
            elif (operacion == 0):
                Impresion.impresion_basica(mensaje_fin_programa)
                break
            else:
                continue



# MENÚS

def formar_menu_empleados_rasos():
    menu_lista = ""
    menu = ""
    lista_empleados = []
    for empleado in empresa:
        if (empleado.departamento != "JEFAZOS"):
            lista_empleados.append(empleado.nombre)
    menu_lista = list(enumerate(lista_empleados,start = 1))
    for num,elem in menu_lista:
        menu += f'{num} - {elem}\n'
    total = len(menu_lista)
    return menu, total, menu_lista

def formar_menu_plantilla():
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


def cambiar_departamento():
    menu, lim, listado = formar_menu_empleados_rasos()
    empleado = ""
    num = Introduccion.introducir_operacion(menu)
    operacion = Validaciones.validar_enteros(num)
    operacion = Validaciones.validar_rango(operacion,lim)
    if (operacion == -1):
        cambiar_departamento()
    else:
        nuevo_departamento = Introduccion.introducir_operacion("Introduce el nuevo departamento: ")
        for num, elem in listado:
            if (num == operacion):
                empleado = elem
        for para_cambiar in empresa:
            if (para_cambiar.nombre == empleado):
                #para_cambiar.departamento = nuevo_departamento
                para_cambiar.modificar_departamento(nuevo_departamento)
        Impresion.impresion_departamentos(empresa)

def calcular_salario():
    nomina = 0
    elemento = []
    for empleado in empresa:
        if (empleado.departamento != "JEFAZOS"):
            elemento.append(empleado.nombre)
            horas = Introduccion.introducir_operacion(f'¿Cuántas horas ha hecho {empleado.nombre}? --> ')
            horas_num = Validaciones.validar_enteros(horas)
            if (horas_num == -1):
                calcular_salario()
            else:
                elemento.append(horas_num)
                elemento.append(empleado.calcular_salario(horas_num))
        else:
            elemento.append(empleado.nombre)
            elemento.append(0)
            elemento.append(empleado.sueldo)

        Impresion.mostrar_nomina_mes(elemento)

def mostrar_info_individual():
    menu, lim, listado = formar_menu_plantilla()
    empleado = ""
    individuo = Introduccion.introducir_operacion(menu)
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
                Impresion.impresion_basica("\n== IMPRIMIENDO INFORME...")
                para_mostrar.imprimir_info()
        

if __name__ == "__main__":
    main()


