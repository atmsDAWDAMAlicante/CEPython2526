


#Ejercicio 3

def validar_enteros(func):
    def envoltorio(num): 
        try: 
            num = int(num)
            print(f"{num} es un entero")
            func(num)
        except ValueError:
            print("Error: Debe introducir un número entero.")
            return
    return envoltorio

@validar_enteros
def pedir_numero_llamadas(num):
    print(f"Número de llamadas a facturar: {num}")
    horas = 0
    for i in range(num):
        horas += pedir_horas(num)


    print(f'Horas: {horas}')

@validar_enteros
def pedir_horas(horas):
    print(horas)  
pedir_numero_llamadas(input("Introduzca nº de llamadas a facturar: "))

#Ejercicio 4





