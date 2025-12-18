from ejercicios.repaso_examen.REPASO_funciones import *

import os
try:
    os.system('cls')
except:
    os.system('clear')

linea = "===================================="

print(f"{linea}\nMENÚ\n{linea}")

def main():
    while True:
        opcion = input("Selecciona una opción (1-3) o '0' para salir: ")
        try: 
            opcion = int(opcion)
        except ValueError:
            print("Por favor, introduce un número válido.")
        else:
            if (opcion == 1):
                print(buscar())
            elif(opcion == 2):
                lista = [1,2,3,4,5,5]
                lista2 = list(map (lambda x: x*10,lista))
                print(lista2)
            elif(opcion == 3):
                factorial(9)

            elif(opcion==5):
                nuevo = input("Nuevo: ")
                if (nuevo in agenda.keys()):
                    print ("Ya está")
                else:
                    agenda[nuevo] = {}
                    edad = input("Edad")
                    calle = input("Calle")
                    ciudad = input("Ciudad")
                    agenda[nuevo] = {"edad":edad, "calle": calle, "ciudad": ciudad}
            elif(opcion==6):
                nombre = input("Cambiar ciudad")
                if (nombre in agenda.keys()):
                    ciudadNueva = input("Ciudad nueva: ")
                    agenda[nombre]["ciudad"] = ciudadNueva
                    print(agenda[nombre]["ciudad"])
            elif(opcion==7):
                for i in enumerate(agenda):
                    print(i)
                tupla1 = ("Hola", "Adios")
                tupla2 = (1, 2)
                tupla3 = ("jñkl",4)
                diccionarioX = dict(zip(tupla1,tupla2))
                print(diccionarioX)
                diccionario2 = {"Palabra": 11, "Eso": 34}
                #diccionario2.update(dict(tupla3))
                print(dict(tupla3))
                print(diccionario2)
            elif(opcion==8):
                pass
            elif(opcion==9):
                pass
            elif(opcion==10):
                for key in agenda.keys():
                    print(f'Sujeto: {key}:')
                    for key2,value2 in agenda[key].items():
                        print(f'{key2} - {value2}')









            elif (opcion == 0):
                print("Saliendo del menú.")
                break
            else:
                print("un número del 1 al 3, o el 0 para salir")
        finally:
            print(linea)
main()