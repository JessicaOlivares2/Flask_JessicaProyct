from flask import Flask, render_template

app = Flask(__name__)

with app.app_context() :
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/generos/tracks')
def musicas():
    base_de_datos = db.get_db()
    consulta = """
       SELECT t.name,p.name as Artista from tracks t
       JOIN albums a on t.TrackId = a.AlbumId
       JOIN artists p on a.AlbumId = p.ArtistId
       ORDER by t.name asc
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("tracks.html",musicas=lista_de_resultado)

