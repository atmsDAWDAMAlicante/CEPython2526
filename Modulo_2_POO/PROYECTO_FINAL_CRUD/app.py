from flask import Flask, render_template, request, redirect # render para renderizar HTML
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


@app.route("/nuevo_libro", methods=["GET", "POST"])
def nuevo_libro():

    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]

        connection = get_connection()

        with connection.cursor() as cursor:
            sql = "INSERT INTO libros (titulo, autor) VALUES (%s, %s)"
            cursor.execute(sql, (titulo, autor))

        connection.commit()
        connection.close()

        return redirect("/libros")

    return render_template("nuevo_libro.html")


# NUEVA RUTA: PARA ELIMINAR

@app.route("/eliminar_libro/<int:id>")
def eliminar_libro(id):

    connection = get_connection()
    
    with connection.cursor() as cursor:
        sql = "DELETE FROM libros WHERE id = %s"
        cursor.execute(sql, (id,))
    
    connection.commit()
    connection.close()

    return redirect("/libros")















if __name__ == "__main__":
    app.run(debug=True)