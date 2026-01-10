from vista import Introduccion, Impresion


class Empleado:
    def __init__ (self, id, nombre, sueldo, departamento):
        self.id = id
        self.nombre = nombre
        self.sueldo = sueldo
        self.departamento = departamento

    def calcular_salario(self, horas_trabajadas):
        paga_extra = 0
        if (horas_trabajadas > 40):
            horas_extra = horas_trabajadas - 40
            paga_extra = (horas_extra * (self.sueldo / 40))
        
        return self.sueldo + paga_extra

    def modificar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        print(f'{self.nombre}: ahora forma parte de {self.departamento}')

    def imprimir_info(self):
        longitud = len(f'{self.nombre}: {self.id} {self.sueldo} € {self.departamento}')  + 1
        lineas = "-" * longitud
        print(lineas)
        print(f'EMPLEADO: {self.nombre}\nCódigo: {self.id}\nSalario: {self.sueldo} €\nDepartamento: {self.departamento}')
        print(lineas)


# Creación de los empleados del ejercicio
empresa = []
empresa.append(Empleado("E7876", "JABBA THE HUTT", 2000, "CONTABILIDAD"))
empresa.append(Empleado("E7888", "PRINCESA LEIA", 4500, "JEFAZOS"))
empresa.append(Empleado("E7845", "HAN SOLO", 1000, "VENTAS"))
empresa.append(Empleado("E7822", "LUKE SKYWALKER", 1550, "OPERACIONES"))


class Validaciones():
    @staticmethod
    def validar_enteros(num):
        try:
            num = int(num)
        except ValueError:
            Impresion.impresion_basica("Introduzca un entero positivo: ")
            return -1
        else:
            return int(num)
    
    @staticmethod
    def validar_rango(num,lim):
        if (num <= lim) and (num >=0):
            return int(num)
        else:
            Impresion.impresion_basica(f'Introduzca un entero entre 0 y {lim}')
            return -1