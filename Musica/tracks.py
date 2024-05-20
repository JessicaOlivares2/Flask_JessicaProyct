from flask import Blueprint,Flask, render_template
from . import db

bp = Blueprint('tracks', __name__,url_prefix= '/tracks')
app = Flask(__name__)

@bp.route('/<int:id>')
def tracks():
    base_de_datos = db.get_db()
    consulta = """
       SELECT t.name,p.name as Artista from tracks t
       JOIN albums a on t.TrackId = a.AlbumId
       JOIN artists p on a.AlbumId = p.ArtistId
       ORDER by t.name asc
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("tracks.html",generos=lista_de_resultado)



