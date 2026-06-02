# PROYECTO: Aplicación con Flask y MySQL.  

Desarrollar una aplicación web completa, utilizando Python y Flask, conectada a una base de datos MySQL, simulando un sistema real de gestión empresarial.

El **proyecto** deberá implementar autenticación de usuarios, roles con permisos, CRUD completo de todas las entidades, gestión de ficheros y documentación técnica, aproximándose al funcionamiento de una aplicación real en producción.

## El tema del proyecto es libre, pudiendo basarse en contextos reales, como:
    ✓ Tienda online
    ✓ Clínica médica
    ✓ Gimnasio
    ✓ Biblioteca
    ✓ Taller mecánico
    ✓ Sistema de reservas
    ✓ Plataforma educativa
    ✓ Otro sistema propuesto por tí

## Objetivos:
    ✓ Diseñar una base de datos relacional compleja en MySQL
    ✓ Implementar autenticación de usuarios
    ✓ Gestionar roles y permisos
    ✓ Desarrollar una aplicación web con Flask similar a un entorno real
    ✓ Crear una interfaz web funcional y segura
    ✓ Implementar CRUD completo de todas las entidades
    ✓ Exportar datos a TXT y JSON
    ✓ Documentar y justificar las decisiones técnicas

## BASE DE DATOS:  
Mínimo 4 tablas obligatorias, incluyendo:
    o Usuarios
    o Roles
    o Tabla principal del sistema
    o Tablas secundarias
    o Al menos una tabla intermedia
Claves primarias y foráneas
Integridad referencial
Datos coherentes con el contexto del proyecto

## Proyecto RA 3.3-3.4-3.5
Se deberá entregar un script SQL completo, que incluya:
    − Creación de la base de datos
    − Creación de todas las tablas
    − PK y FK correctamente definidas
    − Registros de prueba
    − Creación inicial de usuarios y roles

## AUTENTICACIÓN Y AUTORIZACIÓN
La aplicación debe implementar un sistema de login:
    • Login mediante formulario
    • Verificación de credenciales contra la base de datos
    • Uso de sesiones (session)
    • Contraseñas:
o Almacenadas cifradas

## ROLES OBLIGATORIOS
La aplicación debe incluir roles de usuario:
Ejemplo mínimo:
    • ADMIN
    • USUARIO  
El ADMIN podrá realizar:  
    − CRUD completo de usuarios
    − CRUD completo de todas las tablas del sistema
El USUARIO podrá:  
    − Acceder al sistema mediante login
    − Visualizar datos permitidos
    − Crear y modificar sus propios registros
    − Acceder únicamente a aquellas tablas que le correspondan
    − No podrá eliminar registros globales

**El control de permisos debe realizarse desde Flask, no solo desde el HTML.**

## CRUD OBLIGATORIO PARA:
    • Usuarios (al menos desde rol administrador)
    • Tabla principal
    • Tablas secundarias

## OPCIÓN DE EXPORTAR FICHEROS (RA 3)
    − Exportación de datos a .txt
    − Exportación de datos a JSON

Proyecto RA 3.3-3.4-3.5
## DOCUMENTACIÓN DEL PROYECTO (RA 5)
El alumnado deberá documentar:
    1. Análisis del sistema
    2. Diseño de la base de datos
    3. Explicación del login y roles, incluyendo usuarios y contraseñas
    4. Explicación del CRUD
    5. Pruebas realizadas, errores y depuración

## MEJORAS OPCIONALES (SUBEN NOTA)
    − Auditoría (logs de acciones)
    − Exportación a PDF
    − API REST
    − Despliegue en WEB

## CRITERIOS DE EVALUACIÓN:
Base de datos: 1 punto  
    • Diseño y relaciones correctas
Login y roles: 1,5 puntos
    • Login funcional
    • Gestión de roles y permisos
CRUD completo: 4 puntos
    • Crear y leer datos
    • Actualizar registros
    • Eliminar registros
    • Seguridad y validaciones
Flask y arquitectura: 1,5 puntos
    • Rutas y templates
    • Organización y claridad del código
Archivos TXT / JSON: 1 punto
    • Implementación correcta
Documentación y pruebas: 1 punto
    • Claridad y profundidad
Mejoras opcionales: hasta +1 punto
    Se podría superar el 10

## ENTREGA: 25 de mayo de 2026
    − Archivo zip con toda la estructura incluyendo requeriments.txt
    − Archivo sql con la base de datos
    − Documentación del proyecto. Pdf o md