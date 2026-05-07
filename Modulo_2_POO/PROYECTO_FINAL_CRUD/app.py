from flask import Flask, render_template # render para renderizar HTML
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
def get_connection():
    return pymysql.connect(
        host="127.0.0.1",   # CAMBIAR Y QUITAR LOCALHOST
        user="root",
        password="",
        database="biblioteca_db",
        port=3306,         # PONER EL PUERTO ESTE QUE ME ESTÁ VOLVIENDO LOCO
        cursorclass=pymysql.cursors.DictCursor
    )

# Ruta principal
@app.route("/")
def home():
    return "<h1>Aplicación Biblioteca funcionando</h1>"

# Ruta para probar conexión a BD
''' ANTES DE ECHARLO TODO A PERDER
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
    '''
# Ruta para probar QUE RENDERIZA
@app.route("/libros")
def ver_libros():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()

    connection.close()

    return render_template("libros.html", libros=libros)

if __name__ == "__main__":
    app.run(debug=True)