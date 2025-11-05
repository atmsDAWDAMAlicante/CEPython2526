# EJERCICIOS - 02 - Modulo - 03 - Bucle For

import os

linea = "===================================="
os.system('cls')
print(f"{linea}\nInicio de los ejercicios de este bloque\n{linea}")


#1. Enunciado: Utilizando cinco bucles tipo for y en cada uno de ellos el tipo range() con tres argumentos,
# escribe el código Python necesario para que se muestre por pantalla la siguiente
# información tabulada con las siguientes cinco series aritméticas:
#1 2 3 4 5 6 7 8 9 10
#2 4 6 8 10 12 14 16 18 20
#20 23 26 29 32 35 38 41 44 47
#10 14 18 22 26 30
#40 35 30 25 20 15 10 5 0
print(f"---Ejercicio nº 1: Cinco bucles para cinco operaciones")
mensaje_ej_1 = "" #Aquí se recogerá el string que se imprimirá por pantalla

#1º Bucle: incremento +1
for i in range(1,11,1):
    mensaje_ej_1 += f"{i:<3}"

mensaje_ej_1 += "\n"

#2º Bucle, incremento +2
for i in range(2,21,2):
    mensaje_ej_1 += f"{i:<3}"

mensaje_ej_1 += "\n"

#3º Bucle, incremento +3 desde 20
for i in range(20,48,3):
    mensaje_ej_1 += f"{i:<3}"

mensaje_ej_1 += "\n"

#4º Bucle: incremento +4 desde 10
for i in range (10,31,4):
    mensaje_ej_1 += f"{i:<3}"

mensaje_ej_1 += "\n"

#5º Bucle: decremento -5 desde 40 hasta 0
for i in range(40,-1,-5):
    mensaje_ej_1 += f"{i:<3}"


#Salida final
print(mensaje_ej_1)    





#2. Enunciado: 
print(f"---Ejercicio nº 2: Dxxx")






#3. Enunciado: 
print(f"---Ejercicio nº 3: Dxxx")






#4. Enunciado: 
print(f"---Ejercicio nº 4: Dxxx")






#5. Enunciado: 
print(f"---Ejercicio nº 5: Dxxx")






#6. Enunciado: 
print(f"---Ejercicio nº 6: Dxxx")






#7. Enunciado: 
print(f"---Ejercicio nº 7: Dxxx")






#8. Enunciado: 
print(f"---Ejercicio nº 8: Dxxx")







#9. Enunciado: 
print(f"---Ejercicio nº 9: Dxxx")



#10. Enunciado: 
print(f"---Ejercicio nº 10: Dxxx")


#11. Enunciado: 
print(f"---Ejercicio nº 11: Dxxx")



#12. ENTREGABLE - Enunciado: 
print(f"---Ejercicio nº 12: Dxxx")






print(f"{linea}\nFin de los ejercicios de este bloque\n{linea}")