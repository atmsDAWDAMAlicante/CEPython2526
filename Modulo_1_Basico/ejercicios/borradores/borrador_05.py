#Prueba de división por cero
try:
    resultado = 4/0
#except ValueError:
except ZeroDivisionError:
    print(ValueError)
    print(f'Error: {ValueError}')
else:
    print(resultado)
finally:
    print("Fin del programa")

'''
Capturar y nombrar excepciones
try:
    int("abc")
except ValueError as e:
    print(type(e))  # <class 'ValueError'>
'''

'''
En C# throw new Exception("Algo salió mal");
En Python raise Exception("Algo salió mal")
'''