import random

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

agenda = {
    "Ana": {"telefono": "600123123", "email": "ana@example.com"},
    "Luis": {"telefono": "611222333", "email": "luis@example.com"}
}

# 2. Funcionamiento del programa
#El programa mostrará un menú en bucle hasta que el usuario elija salir:
    #1. 1. Añadir contacto
    #2. 2. Consultar contacto
    #3. 3. Modificar contacto
    #4. 4. Borrar contacto
    #5. 5. Listar todos los contactos
    #6. 6. Salir
salto = "\n"
despedida = "Hasta pronto\n=== FIN DEL PROGRAMA ==="
menu = ["1. Añadir contacto","2. Consultar contacto","3. Modificar contacto",
"4. Borrar contacto","5. Listar todos los contactos","6. Salir"]


def ejecutar_menu():
    opcion = input(f'Elige una opcion del {menu}\n-- su opción (+Intro): ')
    while True:
        try:
            opcion = int(opcion)
            if (opcion > 0 ) and (opcion < 7):
                print(type(opcion))
                ejecutar_opcion(opcion)
                break
            else:
                print("Intruduzca un número del 1 al 6")
        except ValueError:
            print(f'Introduzca un número entero del 1 al 6')
        opcion = input(f'Elige una opcion ¡¡¡PERO AHORA BIEN!!! {menu}\n-- su opción (+Intro): ')



def ejecutar_opcion(num):
    print(f'Vd. ha seleccionado: {menu[num-1]}')
    if (num == 1):
        anadir_contacto()

    elif (num == 2):
        pass
    elif (num == 3):
        pass
    elif (num == 4):
        pass
    elif (num == 5):
        listar_agenda()
    else:
        print(f'Vd. ha seleccionado: {menu[num-1]}\n{despedida}')


#1 AÑADIR CONTACTO
def anadir_contacto():
    nombre_contacto = input("Introduzca el nombre del nuevo contacto: ")
    if nombre_contacto in agenda:
        print("Ya existe")
        print(f'{nombre_contacto}:{agenda[nombre_contacto]}')
    else:
        print("No existe")
        agenda[nombre_contacto] = ""

        
        datos =[]
        tupla_titulos = ("telefono", "email")
        datos.append(input("Introduce el telefono: "))
        datos.append(input("Introduce el email: "))
        datos = tuple(datos)
        nuevos_datos = {}
        nuevos_datos.update(dict(zip(tupla_titulos,datos)))
        agenda[nombre_contacto] = nuevos_datos
        print(agenda)
        
        '''
        base = ("telefono", "email")
        datos =[]
        nuevo_contacto = {}
        datos.append(input("Introduce el telefono: "))
        datos.append(input("Introduce el email: "))
        print(f'DATOS{datos}')
        nuevo_contacto = zip(base, tuple(datos))
        print(f'DATOS{nuevo_contacto}')
        agenda.update(nuevo_contacto)
        #print(f'Dato introducido.{nombre_contacto}:{agenda[nombre_contacto]}')
        '''
        #listar_agenda()
    #algo_mas()


# 5 LISTAR TODOS LOS CONTACTOS
def listar_agenda():
    for key,value in agenda.items():
        print(f'{key}---{value}')
    algo_mas()


#ALGO MAS---


def algo_mas():
    while True:
        algo_mas=input("¿Desea realizar otra operación: [S/N]: ")
        algo_mas=algo_mas.upper()
        if(algo_mas == "S") or (algo_mas == "SI"):
            ejecutar_menu()
        elif (algo_mas == "N") or (algo_mas == "No"):
            print("Hasta pronto\n=== FIN DEL PROGRAMA ===")
            break
        else:
            print("¿Cómo?")
