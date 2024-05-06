from flask import Flask, render_template

app = Flask(__name__)

with app.app_context() :
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/generos')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("generos.html",generos=lista_de_resultado)