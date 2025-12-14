import os
os.system("cls")
linea = "======================"
#REPASO DE COSAS DEL TEMA 2
#Variables
lista = ["Antonio", "Jose", "Ana", "Luis", "Maria"]
tupla = (1,2,3,4,5,6,7,8,9)
diccionario = {
    "SonGoku":True,
    "Vegeta":False,
    "Freezer":False,
    "Krilin":True
}

#1 - LAS LISTAS
print(f'{linea}\n{"LAS LISTAS":>15}\n{linea}')
print(id(lista))
print(f'Muestra la lista entera lista:\n{lista}')
lista2 = ["Pepe", "Manolo"]
#lista3 = lista + lista2
lista += lista2
#print(f'{id(lista)}-{id(lista2)}-{id(lista3)}')
print(f'{id(lista)}-{id(lista2)}')

#for i in enumerate(lista, start=10):
for i in (range(len(lista)-1, -1, -1)):
    print(i)
    if (lista[i]=="Pepe"):
        del lista[i]
        print("Borrado")
    else:
        print("NO borrado")
eliminadoLista1 = lista.pop(1)
eliminadoLista2 = lista.remove("Maria")
print(eliminadoLista1)
print(eliminadoLista2) #None

print(lista)
try:
    print(lista[34])
except IndexError:
    print("Eso no existe")

if "Pepe" not in lista:
    print("Pepe está fuera")
lista = (sorted(lista))
print(lista)

#2 - LAS TUPLAS
print(f'{linea}\n{"LAS TUPLAS":>15}\n{linea}')









#3 - LOS CONJUNTOS
print(f'{linea}\n{"LOS CONJUNTOS SET":>15}\n{linea}')









#4 - LOS DICCIONARIOS
print(f'{linea}\n{"LOS DICCIONARIOS":>15}\n{linea}')