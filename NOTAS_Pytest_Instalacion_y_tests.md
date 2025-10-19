#NOTAS para instalar y usar PYTEST en Visual Studio Code

##1º Instalación: 
- en la terminal ejecutar: **pip install pytest**
- luego poner pytest en el PATH
- comrpobar la versión en el cmd:  **pytest --version**

##2º En el directorio raiz del proyecto:
- Abrir la ventana con Ctrl+Shift+P
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