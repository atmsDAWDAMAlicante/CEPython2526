

# FUNCIONES GENERALES
# Pedir números
def pedirNumeros(veces):
    resultado = []
    
    while (veces > 0):
        numero = input(f"Introduce un número entero (vez: {veces}): ")
        try:
            numero = int(numero)
            resultado.append(numero)
            veces -= 1
            print(f'{resultado} - veces: {veces}')
            
        except ValueError as e:
            print(f"Error: introduce un entero - {e}") 
            print(f'{resultado} - veces: {veces}') 
    return resultado


def convertir_a_segundos(lista):
    horasAminutos = lista[0]*60
    minutosAsegundos= (horasAminutos*60) + (lista[1]*60)
       
    return minutosAsegundos + lista[2]