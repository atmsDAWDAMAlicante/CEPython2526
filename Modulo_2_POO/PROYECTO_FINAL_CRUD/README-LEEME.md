# Proyecto Biblioteca Flask

Proyecto RA 3.3-3.4-3.5 - Aplicación con Flask y MySQL
Alumno: Ángel Tomás Moreno Senén
Curso de Especialización programacion de aplicaciones en lenguaje Python y Analisis de datos
IES Severo Ochoa, 
Temática: Una biblioteca particular

## Tecnologías utilizadas

IDE: Visual Studio Code
Los siguientes programas han sido utilizados con el paquete XAMPP (Control Panel v3.3.0)
Servidor Apache Puertos 80 y 443
MySQL puerto 3306

Lenguaje Python y Flask

Librerías: contenido de requirementes.txt
Flask
PyMySQL

# Arranque de la aplicación
Es necesario tener levantado el servidor Apache y MySQL con la biblioteca.sql en el directorio sql en la carpeta del proyecto.
En el directorio del proyecto se encuetntra el archivo app.py que ha de ser ejecutado mediante terminal una vez se hayan levantado ambos servidores.
Aunque la aplicación tiene sus funcionalidades naturales, he decidido dejar dentro de la carpeta del proyecto un archivo me ha hecho las veces de índice o índices de links para ir probando con el navegador y su nombre es LEEME O ABREME CON LA APP EN MARCHA.html

# Funcionamiento de la aplicación.
Lo primero que pide la aplicación es autenticarse.
Hay varios ususarios en la base de datos.
Con el rol de administrador está:
ususario: admin
password: 9876

Otro usuario normal:
usuario: pepe
password: 0000

Otro usuario normal:
usuario: ana
password: 123

Una vez autenticado el usuario, si se trata del administrador, este podrá crear libros nuevos, editar y eliminar de la biblioteca. Ver en el navegador una lista de los libros en txt o en JSON.


El resto de usuarios sólo podrá verlos.


## Base de datos

## Sistema de login y roles

## CRUD de libros

## Exportación de datos

## Problemas encontrados y soluciones

## Mejoras futuras

## Conclusión