from flask import Blueprint, render_template
from . import db
bp = Blueprint('genero', __name__,url_prefix= '/genero')
@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero.html",generos=lista_de_resultado)

@bp.route('/<init:db>')
def detalle(id):
    con = db.get_db()
    consulta1 ="""
    SELECT name from genres
    where GenreId = ?;
    """
    consulta2 = """
    SELECT t.name,g.name as Genero from tracks t
    JOIN albums a on t.TrackId = a.AlbumId
    JOIN artists p on a.AlbumId = p.ArtistId
    JOIN genres g on p.ArtistId = g.GenreId
    ORDER by g.name asc
    """
    res =con.execute(consulta1,(id,))
    genero = res.fetchone()
    res =con.execute(consulta2,(id,))
    lista_de_resultado = res.fetchall()

    pagina = render_template('detalle_genero.html',
    genero = genero,
    canciones = lista_de_resultado)
    return pagina

