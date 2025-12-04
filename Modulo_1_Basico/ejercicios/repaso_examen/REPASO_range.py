import os
os.system('cls')
linea = "===================================="
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")

#1 Mostrar un range
print(f"---Ejercicio nº 1: Mostrar un range")
rango1 = range(0,50,2)
rango2 = range(90,30,-5) 
#rint(tuple(rango1))
print(list(rango1))
print(list(rango2))
print(len(rango1))
print(sum(rango1))
print(list(rango1)+list(rango2))
