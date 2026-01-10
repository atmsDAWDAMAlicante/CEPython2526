


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
    def impresion_basica(texto):
        print(texto)

    @staticmethod
    def impresion_departamentos(empresa):
        print("---> Distribución por departamentos:")
        for empleado in empresa:
            print(f'Empleado/a: {empleado.nombre} -> departamento: {empleado.departamento}')
        print("-" * 10)

    @staticmethod
    def mostrar_info_toda_la_empresa(empresa):
        print("=" * 25)
        print("== IMPRIMIENDO INFORME...")
        for elemento in empresa:
            print(f'{elemento.id} - NOMBRE: {elemento.nombre}:')
            print(f'Departamento: {elemento.departamento} / Salario base: {elemento.sueldo}')
        print("== Informe completado")
        print("=" * 25)

    @staticmethod
    def mostrar_nomina_mes(elemento):
        print(elemento)