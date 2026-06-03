# Proyecto Biblioteca Flask  
# NOTA: PARA LA RECUPERACIÓN DEL DÍA 04/06/2026

Proyecto RA 3.3-3.4-3.5 - Aplicación con Flask y MySQL  
Alumno: Ángel Tomás Moreno Senén  
Curso de Especialización programacion de aplicaciones en lenguaje Python y Analisis de datos  
IES Severo Ochoa, Elx  
Temática: Una biblioteca particular  

Este proyecto ha sido revisado y corregido varias veces durante los últimos días debido a errores indicados en la primera entrega.

Las sucesivas correcciones las he ido subiendo a GitHub en varias carpetas sucesivas para asegurarme no estropear el proyecto.

La URL de la última carpeta, que es la *VERSIÓN QUE SE ENTREGA EN ESTA RECUPERACIÓN*, es:
https://github.com/atmsDAWDAMAlicante/CEPython2526/tree/main/Modulo_2_POO/PROYECTO_FINAL_CRUD_BISES/PRUEBA_FINAL

El resto de carpetas sucesivas están en:
https://github.com/atmsDAWDAMAlicante/CEPython2526/tree/main/Modulo_2_POO/PROYECTO_FINAL_CRUD_BISES

La primera carpeta: URL al repositorio de GitHub donde comprobar los commits hechos durante el desarrollo
https://github.com/atmsDAWDAMAlicante/CEPython2526/tree/main/Modulo_2_POO/PROYECTO_FINAL_CRUD


## 1.- Tecnologías utilizadas  

IDE: Visual Studio Code  
Los siguientes programas han sido utilizados con el paquete XAMPP (Control Panel v3.3.0)  
Servidor Apache Puertos 80 y 443  
MySQL puerto 3306  

Lenguaje Python y Flask  

Librerías: contenido de requirementes.txt  
Flask
PyMySQL
werkzeug

## 2.- Arranque de la aplicación  
Es necesario tener levantado el servidor Apache y MySQL con la biblioteca.sql en el directorio sql en la carpeta del proyecto.  

En el directorio del proyecto se encuetntra el archivo app.py que ha de ser ejecutado mediante terminal una vez se hayan levantado ambos servidores.  

## 3.- Funcionamiento de la aplicación, login y roles  
### 3.1 - Login y roles
Lo primero que hace la aplicación es pedir autenticación mediante usuario y contraseña.  

Al empezar hay tres ususarios en la base de datos.  

Administrador y usuarios normales pueden ver en el navegador 
una lista de los libros en txt o en JSON haciendo clic en la opción del menú

Con el rol de **administrador** está:  
ususario: admin  
password: 9876  

**Otro usuario normal**:  
usuario: pepe  
password: 0000  

**Otro usuario normal**:  
usuario: ana  
password: 1234  

**La aplicación muestra el nombre del usuario conectado**

### 3.2 - Administrador
#### 3.2.1 - Gestión de libros
Solo el administrador puede crear libros nuevos, editar y eliminar los que ya hay en la biblioteca. 
La aplicación no permite crear libros si no se pone algún dato en el autor y/o en el título.

#### 3.2.1 - Gestión de usuarios
Solo administrador puede crear, editar y eliminar nuevos usuarios. 
Y es el único que puede ver esta opción en el menú de la aplicación


### 3.3 - Usuarios normales
#### 3.3.1 - Gestión de libros
Pueden ver los libros.
En el menú puede ver la opción "Añadir libro", "Editar" y "Eliminar" pero si hace clic en alguna de estas opciones la aplicación le muestra 
"No tienes permisos".

El usuario puede reservar libros. **Los libros reservados quedan registrados en la**  
**base de datos MySQL (comprobable desde phpMyAdmin).**

El usuario normal no puede ver en el menú la opción Usuarios.
 
### 3.4 Autenticación y contraseñas cifradas

La aplicación implementa un sistema de autenticación basado en formulario web.  

El usuario debe introducir su nombre de usuario y contraseña, que son validados con los registros almacenados en la base de datos MySQL.  

Como requisito del ejercicio, las contraseñas no se almacenan en texto plano, están cifradas mediante hash, evitando el acceso directo a las credenciales originales.  

Una vez autenticado el usuario, se crea una sesión en Flask utilizando `session`, lo que permite mantener al usuario identificado durante la navegación por la aplicación.  

## 4.- Base de datos  

La aplicación utiliza una base de datos MySQL denominada `biblioteca_db`.  

Descripción de las tablas:  

- categorias
- libros
- prestamos
- roles
- usuarios
**La estructura incluye una relación de tipo muchos a muchos, implementada mediante una tabla intermedia entre libros y categorías.**  


La base de datos se encuentra definida en un script SQL que está en la carpeta `sql` del proyecto, que incluye:  
- creación de tablas
- claves primarias y foráneas
- y unos datos de prueba


## 5.- Exportación de datos  

La aplicación permite la exportación de datos de la biblioteca en dos formatos:  

### 5.1.- Exportación a TXT  
Genera un archivo de texto plano con el listado de libros y se muestra en el navegador.  

### 5.2.- Exportación a JSON  
Se genera un archivo en formato JSON con la información estructurada de los libros.  
Este formato permite su reutilización.  

## 6.- Problemas encontrados y soluciones  
Durante el desarrollo del proyecto se han producido varios problemas técnicos que lo han complicado mucho.  

### 6.1.- Conexión a la base de datos (puerto 3306)  
La conexión con MySQL. En algunos momentos la aplicación no podía conectarse correctamente debido a que el servidor no estaba iniciado o el puerto 3306 estaba siendo utilizado por otro proceso.  

La solución consistió en comprobar que tanto Apache como MySQL estuvieran correctamente iniciados desde XAMPP antes de ejecutar la aplicación Flask.  

### 6.2.- Errores en rutas de la aplicación  
Se produjeron errores de tipo "Not Found" al acceder a determinadas rutas, causados por enlaces mal construidos en las plantillas HTML utilizando incorrectamente variables de Jinja2.  

Se solucionó revisando las rutas definidas en Flask y corrigiendo la sintaxis de los enlaces.  

### 6.3.- Gestión de sesiones  
Inicialmente la sesión de usuario no se controlaba correctamente, y provocó accesos no deseados a determinadas funcionalidades.  

Se solucionó implementando correctamente el uso de `session` en Flask y protegiendo las rutas sensibles mediante comprobaciones de autenticación.  

### 6.4.- Seguridad de contraseñas  
Al principio las contraseñas se almacenaban en texto plano, lo que supone un problema de seguridad.  

Este aspecto se mejoró implementando el uso de hash para el almacenamiento de contraseñas en la base de datos.  

  

# 7.- Conclusión  

El proyecto ha sido desarrollado y revisado en varias etapas (que se pueden comprobar en GitHub) hasta llegar a una versión funcional completa.

Durante el proceso se han corregido errores importantes relacionados con la autenticación, la gestión de usuarios y la coherencia entre la base de datos y la aplicación.

*No me ha dado más tiempo a mejorar su aspecto con CSS ni a añadir botones de navegación.*   

**Se entrega el proyecto en este estado como versión final para la recuperación.**.  

*Muchas gracias y disculpe los problemas técnicos.*  
Ángel Tomás Moreno Senén