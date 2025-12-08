import os
os.system("cls")

def amumentar_directiva(**kwargs):
    directiva.update(kwargs)
    imprime_directiva() #Ahora se imprime el resultado

def imprime_directiva():
    print(directiva)
    for clave, valor in directiva.items():
        print(f'{clave}: es {valor}')


def buscar_directiva(nombre):
    print("____________________")
    print(type(nombre))
    #nombre = str(nombre)
    encontrado = False
    for clave,valor in directiva.items():
        if nombre.lower() in valor.lower():  # búsqueda parcial
            print(f'{valor} se encuentra en la directiva como {clave}')
            encontrado = True
    if not encontrado:
        print(f'No hay ningún miembro que coincida con: {nombre}')


# Inicio del programa, se forma la directiva:
tupla_cargo = ("Presidente", "Vicepresidente", "Tesorero")
tupla_nombres = ("Paco", "Pepe", "Luis")
directiva = dict(zip(tupla_cargo,tupla_nombres))
#directiva.setdefault("Vocal")

# Se llama a la función para aumentar la directiva
amumentar_directiva(Vocal1= "Jose Luis", Vocal2= "Manolo")

# Por último se buscan miembros de la directiva
buscar_directiva("nol")
buscar_directiva("Federico")