# Ejercicio facilitado por el ChatGPT

#✏️ EJERCICIO TÍPICO con decoradores
#Crea un decorador llamado validar_entero_positivo que:
#compruebe que el valor recibido es un entero mayor que 0

    #Si no lo es, muestre un mensaje de error
    #Si lo es, permita ejecutar la función

#Crea dos funciones:
    #calcular_cuadrado(numero) → muestra el cuadrado
    #calcular_triple(numero) → muestra el triple

#Ambas funciones deben usar el decorador.

#🧩 Pistas (no mires la solución aún)
    #El decorador debe convertir a int
    #Usa try / except
    #Usa @decorador
    #Las funciones no validan, solo calculan

import os
os.system('cls')

# SE PONE ARRIBA EL DECORADOR!!!!!!!!!!!!!!!!!!

# Segundo paso: crear el decorador
def validar_entero_positivo(func): #función decoradora
    def envoltorio(num):
       try:
           num = int(num)
           return func(num) # ESTO LLAMA A LA FUNCIÓN DECORADA
       except ValueError:
           print("¡Error: introduce un número entero!")
           main()
    return envoltorio 
    # ¿Esto qué hace? Ayuda del ChatGPT:
    # El return envoltorio permite que la función original sea sustituida 
    # por la función decorada, mientras que el return func(...) 
    # devuelve el resultado de la ejecución de la función original.

# Primer paso: crear las dos funciones sin decorador
@validar_entero_positivo
def calcular_cuadrado(num):
    resultado = num ** 2 
    return resultado

@validar_entero_positivo
def calcular_triple(num):
    resultado = num * 3
    return resultado




def main():
    num = input("Introduce un número entero: ")
    print(f"El cuadrado de {num} es {calcular_cuadrado(num)}")
    print(f"El triple de {num} es {calcular_triple(num)}")
    salir(input("¿Otra vez? (s/n): "))
    
    
def salir(vez):
    if (vez.lower() == 's'):
        main()
    elif (vez.lower() == 'n'):
        print("=== Fin del programa ===")
        return
    else:
        print("¿Otra partidita de ajedrez, Dave?")
        salir(input("¿Otra vez? (s/n): "))

main()