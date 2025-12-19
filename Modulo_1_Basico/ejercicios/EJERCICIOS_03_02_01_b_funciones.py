

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

# Ejercicio 1
def convertir_a_segundos(lista):
    horasAminutos = lista[0]*60
    minutosAsegundos= (horasAminutos*60) + (lista[1]*60)
       
    return minutosAsegundos + lista[2]


# Ejercicio 2
def suma_tiempos(tiempos):
    horas = 0
    minutos = 0
    segundos = 0
    
    for t in tiempos:
       horas += t[0]
       minutos += t[1]
       segundos += t[2]
    
    tiempo = []
    tiempo.append(horas)
    tiempo.append(minutos)
    tiempo.append(segundos)
    print(tiempo)
    acumular_excesos(tiempo)

def acumular_excesos(tiempo):
    
    horas, minutos, segundos = tiempo
    tiempo_final = [horas,0,0]
    if (segundos > 59):
        tiempo_final[1]+= segundos//60
        tiempo_final[2]+= segundos%60
    if (minutos > 59):
        tiempo_final[0]+= minutos//60
        tiempo_final[1]+= minutos%60
    print(f'Tiempo total: {tiempo_final[0]} h: {tiempo_final[1]} m: {tiempo_final[2]} s')

    #Ejercicio 3
    