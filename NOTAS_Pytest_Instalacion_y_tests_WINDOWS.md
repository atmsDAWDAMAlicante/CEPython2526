# NOTAS para instalar y usar PYTEST en Visual Studio Code
# *Instalación de pytest en VSC* en **WINDOWS**

## 1º Instalación: 
- en la terminal ejecutar: **pip install pytest**
- luego poner pytest en el *PATH*
- comrpobar la versión en el *cmd*:  **pytest --version**

## 2º En el directorio raiz del proyecto:
- Abrir la ventana con *Ctrl+Shift+P*
- ejecutar en esta venanta **Python: Configure Tests**
- Seleccionar: **pytest framework**

VS Code creará un archivo __.vscode/settings.json__:
```
{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}

```
ó
```
{
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["."],
  "python.testing.unittestEnabled": false,
  "python.testing.nosetestsEnabled": false
}

```

## 3º Ficheros y directorios
- Dentro de la carpeta de cada tema crear dos directorios: ejercicios y tests
- Dentro de ambas carpetas hay que crear un fichero (vacío) llamado: **__init__.py**

## 4º Diseño del archivo test_suma.py
- Se crea dentro de la carpeta tests
- Contenido:
```
import pytest
from ejercicios.prueba_sumar import sumar

def test_sumar():
    assert sumar(2,4) == 6
```
- Suponiendo que en el directorio "*ejercicios*" hay un archivo "*prueba_sumar.py*" con una función sumar que recoge dos enteros y devuelve un entero.

## 5º Ejecución del test
- Rápida: en la terminal, para ejecutar todos los tests: **pytest**
- Para ejecutar sólo un test: en el directorio raiz de ejercicios/tests: **pytest tests/test_suma.py**
