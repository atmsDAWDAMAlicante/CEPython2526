# EJERCICIOS_01_Clases_y_objetos_sencillos

# Ejercicio 10 - ENTREGABLE - ENUNCIADO: 
# Escribe una clase de Python Empleado con atributos:
    # id: identificador del empleado
    # nombre: nombre completo del empleado
    # sueldo: pago base correspondiente a 40 horas de trabajo
    # departamento: departamento al que pertenece

# Como métodos:
    # __init___
    # calcular_salario,
    # modificar_departamento
    # imprimir_info

# Datos de muestra de empleados:
    # ID NOMBRE SUELDO DEPARTAMENTO
    # E7876 JABBA THE HUTT 2000 € CONTABILIDAD
    # E7888 PRINCESA LEIA 4500 € JEFAZOS
    # E7845 HAN SOLO 1000 € VENTAS
    # E7822 LUKE SKYWALKER 1550 € OPERACIONES
 
# Utiliza el método 'modificar_departamento' con el argumento del departamento, 
# para cambiar dicho departamento por otro.

# Usa el método 'imprimir_info' para imprimir los detalles de un empleado.
# El método 'calcular_salario' utiliza como argumento las horas_trabajadas, 
# que es el número total de horas trabajadas por el empleado. 

# Si el número de horas trabajadas es superior a 40, el método calcula las horas 
# extras y las suma al sueldo. Utilizar las siguientes fórmulas:
    # horas_extras = horas_trabajadas - 40
    # paga_extra = (horas_extras * (sueldo / 40))

# El salario final será la suma del sueldo base y la paga por horas extra.
# Además de definir la clase realiza un código donde se pruebe la información anterior.
    # 1. Crea los cuatro trabajadores con los datos dados.
    # 2. Imprime toda su información.
    # 3. Cambia de departamento a Han Solo y a Luke Skywalker 
        # a dos departamentos nuevos.
    # 4. Calcula el salario de todos y muéstralo, teniendo en cuenta que 
        # todos hacen más de 40 horas menos el jefazo. Inventa las horas totales 
        # trabajadas de cada uno. Muestra los nombres y sueldos de los que 
        # su salario es diferente al sueldo base.
import decimal
import os
os.system('cls')

# Modelo
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
        print(f'EMPLEADO: {self.nombre}\nId/Código: {self.id}\nSalario: {self.sueldo} €\nDepartamento: {self.departamento}')
        print("-" * 30)


empresa = []
empresa.append(Empleado("E7876", "JABBA THE HUTT", 2000, "CONTABILIDAD"))
empresa.append(Empleado("E7888", "PRINCESA LEIA", 4500, "JEFAZOS"))
empresa.append(Empleado("E7845", "HAN SOLO", 1000, "VENTAS"))
empresa.append(Empleado("E7822", "LUKE SKYWALKER", 1550, "OPERACIONES"))


# VISTA
class Informes():
    @staticmethod
    def informe_empresa(empresa):
        print(f'{"*" * 5} INFORME: PLANTILLA {"*" * 5}')
        for elemento in empresa:
            elemento.imprimir_info()
        print(f'\n{"_" * 30}')

    @staticmethod
    def informe_salario(empresa):
        print(f'{"*" * 5} INFORME: SALARIO {"*" * 5}\n{"_" * 30}')
        for elemento in empresa:
            if (elemento.departamento != "JEFAZOS"):
                print(f'Empleado: {elemento.nombre}: {decimal.Decimal(elemento.calcular_salario(45))} €')

    @staticmethod
    def info_modificar_departamento():
        for i in empresa:
            if i.nombre == "HAN SOLO":
                print(i.departamento)



# CONTROLADOR

def main():
    Informes.informe_empresa(empresa)
    for nombre in empresa:
        if nombre.nombre == "HAN SOLO":
            nombre.modificar_departamento("RECURSOS HUMANOS")
        elif nombre.nombre == "LUKE SKYWALKER":
            nombre.modificar_departamento("CONTROL DE CALIDAD")
    
    Informes.informe_salario(empresa)
    Informes.info_modificar_departamento()
if __name__ == "__main__":
    main()


