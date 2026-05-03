from flask import Flask
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",       # cambia si usas otro usuario
        password="",       # en XAMPP suele estar vacío
        database="biblioteca_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# Ruta principal
@app.route("/")
def home():
    return "<h1>Aplicación Biblioteca funcionando</h1>"

# Ruta para probar conexión a BD
@app.route("/libros")
def ver_libros():
    connection = get_connection()
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM libros")
            libros = cursor.fetchall()
    finally:
        connection.close()

    resultado = "<h2>Listado de libros</h2><ul>"
    for libro in libros:
        resultado += f"<li>{libro['titulo']} - {libro['autor']}</li>"
    resultado += "</ul>"

    return resultado

if __name__ == "__main__":
    app.run(debug=True)