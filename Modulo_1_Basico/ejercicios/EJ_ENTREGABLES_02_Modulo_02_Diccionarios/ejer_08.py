#EJERCICIOS NTREGABLES UD 02 - Modulo 02 - Diccionarios
#Ejercicio nº 8 
# ALUMNO: ANGEL TOMÁS MORENO SENÉN# 

# Enunciado: Una vez hecho todo lo anterior ten en cuenta que durante el
#partido se produjeron tres sustituciones. Xabi Alonso, Pedrito y Villa abandonaron el
#campo. Navas, Fàbregas y Torres se incorporaron. Haz una copia del diccionario
#“titulares” y asígnale el nombre “final”. Utilizando los métodos setdefault(key,valor) y
#pop(key), elimina del diccionario final a los tres jugadores que fueron sustituidos y añade
#a los que se incorporaron. Muestra al final del ejercicio el contenido del diccionario final




print(f"---Ejercicio nº 8: Cambios de los titulares")

# El diccionario titulares está definido al comienzo de los ejercicios.

titulares = {
1: "Iker Casillas",
15: "Sergio Ramos",
3: "Gerard Piqué",
5: "Carles Puyol",
11: "Joan Capdevila",
14: "Xabi Alonso",
16: "Sergio Busquets",
8: "Xavi Hernández",
18: "Pedro Rodríguez",
6: "Andrés Iniesta",
7: "David Villa"
}

# Comienza la final
#final = titulares #esto copia la referencia en memoria
final = titulares.copy() # esto crea una copia independiente
print (len(final))
# Dorsales de 14: Xabi Alonso, 18: Pedrito y 7: Villa
# Sale Xabi Alonso
sale = final.pop(14)
print (f'Sale {sale}')
# Sale Pedrito
del final[18]
print (len(final))
# Sale Villa
sale = final.pop(7)
print (f'Sale {sale}')
# Entran 22: Navas, 10: Fàbregas y 9: Torres 
final.setdefault(22,"Navas")
final.setdefault(10,"Fàbregas")
final.setdefault(9,"Torres")
# Imprimir resultado
for dorsal, jugador in sorted(final.items()):
    print (dorsal, jugador, sep = " ******** ")