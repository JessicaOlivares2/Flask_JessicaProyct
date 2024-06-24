from flask import Blueprint, render_template
from . import db
bp = Blueprint('track', __name__,url_prefix= '/track')
@bp.route('/')
def tracks():
    base_de_datos = db.get_db()
    consulta = """
        select name,TrackId from tracks
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("track.html",tracks=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 ="""
 
    SELECT t.name,t.Milliseconds,t.Composer,g.name as Genero,p.name as artista,a.Title as titulo, g.GenreId as idG,p.ArtistId as idA,a.AlbumId as idAlb  from tracks t
    JOIN albums a on t.AlbumId = a.AlbumId
    JOIN artists p on a.ArtistId = p.ArtistId
    JOIN genres g on t.GenreId = g.GenreId	
    WHERE t.TrackId = ?
    ORDER BY t.name ASC;

    """
    res =con.execute(consulta1,(id,))
    track = res.fetchone()


    pagina = render_template('detalle_track.html',
    track = track)
    return pagina