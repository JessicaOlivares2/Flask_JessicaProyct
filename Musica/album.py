from flask import Blueprint, render_template
from . import db
bp = Blueprint('album', __name__,url_prefix= '/album')
@bp.route('/')
def albums():
    base_de_datos = db.get_db()
    consulta = """
        select title,AlbumId from albums
        ORDER by title;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("album.html",albums=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 ="""
    select title,AlbumId from albums
    where AlbumId = ?;
    """
    
    consulta2 = """
    select name,b.Title from artists a
    join albums b on a.ArtistId = b.ArtistId
    WHERE b.AlbumId = ?
    ORDER BY name ASC;
    """
    res =con.execute(consulta1,(id,))
    albums = res.fetchone()
    res =con.execute(consulta2,(id,))
    artistas = res.fetchall()

    pagina = render_template('detalle_album.html',
    albums = albums,
    artistas = artistas)
    return pagina
