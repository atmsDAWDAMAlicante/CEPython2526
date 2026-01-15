
# CLASE CON MÉTODOS ESTÁTICOS PARA REALIZAR OPERACIONES VARIAS

# Introducir opciones
class Introduccion():
    @staticmethod
    def introducir_operacion(texto):
        operacion = input(texto)
        #Validaciones.validar_enteros(operacion)
        return operacion
    

# Impresión por consola
class Impresion():
    @staticmethod
    def impresion_basica(texto): # PARA LA IMPRESIÓN DE UN STRING PASADO POR PARÁMETRO
        print(texto)

    # PARA LA IMPRESIÓN DE LOS RESULTADOS DE LAS DISTINTAS OPERACIONES DE LA CLASE EMPLEADO

    # PARA LA IMPRESIÓN DEL CAMBIO DE DEPARTAMENTO
    @staticmethod
    def impresion_departamentos(empresa):
        print("\n---> Distribución por departamentos:")
        print("== IMPRIMIENDO INFORME...")
        for empleado in empresa:
            print(f'Empleado/a: {empleado.nombre} -> departamento: {empleado.departamento}')
        print("== INFORME por DEPARTAMENTOS COMPLETADO\n")
        print("-" * 10)

    # PARA LA IMPRESIÓN DEL CÁLCULO INDIVIDUAL DE LA NÓMINA TRAS INTRODUCIR LAS HORAS EXTRA
    @staticmethod
    def mostrar_nomina_mes(plantilla):
        print("\n---> Cálculo de nóminas:")
        print("\n== IMPRIMIENDO NÓMINAS...")
        for elemento in plantilla:
            print(f'{elemento[0]} ha trabajado {elemento[1]} horas extra: salario: {elemento[2]} €')
        print("== INFORME de NÓMINAS COMPLETADO\n")
        

    # PARA LA IMPRESIÓN DE LA INFORMACIÓN DE TODA LA EMPRESA (No está en la CLASE)
    @staticmethod
    def mostrar_info_toda_la_empresa(empresa):
        print("=" * 25)
        print("\n---> Info de toda la empresa:")
        print("== IMPRIMIENDO INFORME...")
        for elemento in empresa:
            print(f'{elemento.id} - NOMBRE: {elemento.nombre}:')
            print(f'Departamento: {elemento.departamento} / Salario base: {elemento.sueldo}')
        print("== INFORME de toda la empresa COMPLETADO\n")
        print("=" * 25)
    
       
