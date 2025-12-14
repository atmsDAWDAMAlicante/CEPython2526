
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
fin = "==== FIN DEL PROGRAMA ===="

# VALIDACION DEL MENÚ
def validar_menu_principal():
    print(menu)
    operacion = input("Introduce una operacion: ")
    while True:
        try:
            operacion = int(operacion)
            if (operacion > 0) and (operacion < 7):
                return operacion
            else:
                operacion = input("Introduce un entero entre 1-6: ")
        except ValueError:
            print(f"Operación '{operacion}' incorrecta")
            operacion = input("Introduce una operacion, PERO AHORA HAZLO BIEN: ")



# SELECCIÓN DE OPERACIONES
def anadir_contacto():
    contacto = input("Introduzca el contacto: ").strip()
    while True:
        if (contacto in agenda.keys()):
            print("El contacto ya está en la agenda")
            break
        else:
            agenda[contacto] = {}
            telefono = input("Introduce el telefono: ")
            email = input("Introduce el email: ")
            agenda[contacto] = {"telefono": telefono, "email": email}
            print(agenda)
            break

        
def consultar_contacto():
    contacto = input("Introduzca el contacto: ").strip()
    while True:
        if (contacto not in agenda.keys()):
            print("El contacto no existe")
            break 
        elif (contacto in agenda.keys()):
            print(f'El contacto {agenda[contacto]}')
            break

def modificar_contacto():
    contacto = input("Introduzca el contacto: ").strip()
    while True:
        if (contacto not in agenda.keys()):
            print("El contacto no existe")
            break 
        elif (contacto in agenda.keys()):
            print(f'El contacto {agenda[contacto]} existe:')
            telefono = input("Introduce su nuevo teléfono: ")
            email = input("Introduce su nuevo email: ")
            agenda[contacto] = {"telefono":telefono, "email":email}
            print(agenda)
            break

def borrar_contacto():
    contacto = input("Introduzca el contacto: ").strip()
    while True:
        if (contacto not in agenda.keys()):
            print("El contacto no existe")
            break 
        elif (contacto in agenda.keys()):
            agenda.pop(contacto)
            break