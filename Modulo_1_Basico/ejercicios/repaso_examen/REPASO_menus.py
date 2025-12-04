import os
try:
    os.system('cls')
except:
    os.system('clear')

linea = "===================================="

print(f"{linea}\nMENÚ\n{linea}")

def ejecutar_menu():
    while True:
        opcion = input("Selecciona una opción (1-3) o '0' para salir: ")
        if opcion == '0':
            print("Saliendo del menú.")
            break
        try: 
            opcion = int(opcion)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
ejecutar_menu()