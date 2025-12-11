
#LA VARIABLE EN EL MÓDULO
#1. Descripción general
#Crea un programa que mantenga una agenda donde cada contacto tenga:
    #• Nombre (clave principal)
    #• Teléfono
    #• Correo electrónico
#La agenda se guardará en un diccionario de Python, donde:
    #• La clave será el nombre del contacto (cadena).
    #• El valor será otro diccionario con los campos: "telefono" y "email".
#Ejemplo orientativo de estructura (no es necesario imprimirlo tal cual):
# LO PONGO TAL CUAL

agenda = {"Ana": {"telefono": "600123123", "email": "ana@example.com"},
"Luis": {"telefono": "611222333", "email": "luis@example.com"}}

# 2. Funcionamiento del programa
#El programa mostrará un menú en bucle hasta que el usuario elija salir:
    #1. 1. Añadir contacto
    #2. 2. Consultar contacto
    #3. 3. Modificar contacto
    #4. 4. Borrar contacto
    #5. 5. Listar todos los contactos
    #6. 6. Salir
salto = "\n"
menu = f'MENÚ: 1. Añadir contacto - 2. Consultar contacto - 3. Modificar contacto - 4. Borrar contacto - 5. Listar todos los contactos - 6. Salir'

def validar_menu():
    print(menu)
    operacion = input("Introduce una operacion: ")
    while True:
        try:
            operacion = int(operacion)
            if (operacion > 6) or (operacion < 1):
                raise ValueError
            elif (operacion == 6):
                print("Has elegido salir. Hasta pronto.")
                break
            else:
                return operacion
        except ValueError:
            print(f"Operación '{operacion}' incorrecta")
            operacion = input("Introduce una operacion, PERO AHORA HAZLO BIEN: ")
     
        
           


#bifurcacion operaciones
def ejecutar_operacion(num):
    
    print (f'Has elegido {type(num)} operacion {num}')
    if (num == 1):
        validar_menu()
    elif (num == 2):
        pass
    elif (num == 3):
        pass
    elif (num == 4):
        pass
    elif (num == 5):
        pass
        print (agenda)
    else:
        pass
        
        

'''
def formar_diccionario():
    tuplaA = ("Maria", "Luis", "Pepe")
    tuplaB = (4,5,6)
    diccionario = dict(zip(tuplaA,tuplaB))
    print(diccionario)
'''
