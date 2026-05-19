# vamos añadiendio
# render para renderizar HTML
# para el login añadimos session

from flask import Flask, render_template, request, redirect, session #Esto crece
import pymysql
# y subiendo las importaciones



# Crear la aplicación Flask principal
app = Flask(__name__)
# Clave para mantener la sesión iniciada del usuario
app.secret_key = "clave_secreta" #mas corta sin pasarse

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

    # PROTECCIÓN PARA QUE ESTÉ LOGGEADO --- ESTO SE REUTILIZARÁ
    if "usuario" not in session:
        return redirect("/login")
    # VALE, HA FUNCIONADO, TE PIDE QUE TE LOGUEES ANTES DE VER LA BIBLIOTECA

    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()

    connection.close()

    return render_template("libros.html", libros=libros)


@app.route("/nuevo_libro", methods=["GET", "POST"])
def nuevo_libro():

    # REUTILIZANDO--- PROTECCIÓN PARA QUE ESTÉ LOGGEADO 
    if "usuario" not in session:
        return redirect("/login")

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

    # REUTILIZANDO--- PROTECCIÓN PARA QUE ESTÉ LOGGEADO 
    if "usuario" not in session:
        return redirect("/login")

    connection = get_connection()
    
    with connection.cursor() as cursor:
        sql = "DELETE FROM libros WHERE id = %s"
        cursor.execute(sql, (id,))
    
    connection.commit()
    connection.close()

    return redirect("/libros")


@app.route("/editar_libro/<int:id>", methods=["GET", "POST"])
def editar_libro(id):

    # REUTILIZANDO--- PROTECCIÓN PARA QUE ESTÉ LOGGEADO 
    if "usuario" not in session:
        return redirect("/login")

    connection = get_connection()

    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]

        with connection.cursor() as cursor:
            sql = """
            UPDATE libros
            SET titulo = %s, autor = %s
            WHERE id = %s
            """
            cursor.execute(sql, (titulo, autor, id))

        connection.commit()
        connection.close()

        return redirect("/libros")

    else:

        with connection.cursor() as cursor:
            sql = "SELECT * FROM libros WHERE id = %s"
            cursor.execute(sql, (id,))
            libro = cursor.fetchone()

        connection.close()

        return render_template(
            "editar_libro.html",
            libro=libro
        )




# PARA EL LOGIN

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_connection()

        with connection.cursor() as cursor:

            sql = """
                SELECT * FROM usuarios
                WHERE username = %s AND password = %s
            """

            cursor.execute(sql, (username, password))

            usuario = cursor.fetchone()

        connection.close()

        if usuario:

            session["usuario"] = usuario["username"]

            return redirect("/libros")

        else:

            return "Credenciales incorrectas"

    return render_template("login.html")





### TEMPORAL PARA CARGARME LA SESIÓN Y VER QUE VA FUNCIONANDO 
@app.route("/logout")
def logout():

    session.pop("usuario", None)

    return redirect("/login")








if __name__ == "__main__":
    app.run(debug=True)