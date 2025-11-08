# NOTAS para instalar y usar PYTEST en __Visual Studio Code__
# *Instalación de pytest en VSC* en **UBUNTU**

## 1º ## 1º- En una terminal instalar

```
sudo apt install python3.13-venv

```
__alternativa si da error__

```
sudo apt install python3-venv
```

## 2º- Crear un proyecto, abrir uno existente o clonar un repositorio y abrirlo en VSC y una terminal y navegar hasta el directorio donde estarán los ejercicios y los tests con __cd__

## 3º Ejecutar el comando para **crear un entorno virtual**
```
python3 -m venv .venv
```
## 4º **Activar el entorno virtual** (la terminal cambiará a (.venv) __nombre@ubuntu: directorio__)
```
source .venv/bin/activate
```
## 5º **Instalar pytest con el entorno activo**
```
pip install pytest
```
### Comprobación de la instalción
```
pytest --version
```
## 6º Crear un archivo "__requirements.txt__" para reinstalar las dependencias fácilmente en otro entorno.

### 6.1 - Comando para crear el archivo "__requirements.txt__"
```
pip freeze > requirements.txt
```
### 6.2 - Comando para restaurar las dependencias
```
pip install -r requirements.txt
```
## 7º **Configuración de VSCode** para usar el entorno virtual.

En VSC y en la carpeta de ejercicios concreta *abrir la paleta de comandos* (Ctrl + Shift + P): 
```
Python: Select Interpreter
```
Seleccionar en la paleta de comandos:
```
.venv/bin/python
```

## 8º Añadir .venv a *.gitignore*
# En el archivo .gitignore (en la raíz del repositorio)
```
**/.venv/
```

## 9º Para **lanzar los tests**:
```
pytest
```
o, para tener más detalle en la terminal
```
pytest -v

pytest -vv
```

### *NOTA:* _es necesario tener el entorno virtual activo para lanzar los tests, si no dará errores de tipo "pytest: command not found" u otros mensajes de error_
### *NOTA:* _los programas .py se pueden ejecutar con el entorno virtual activo_
### *NOTA:* _el entorno virtual se desactiva con el comando_
```
deactivate
```
_... y desaparecerá el prefijo (.venv) de la terminal._

# CADA VEZ QUE SE ABRA EL PROYECTO
## Dentro del directorio donde esté el archivo _requirements.txt_ EJECUTAR en la terminal:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
