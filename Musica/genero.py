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

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 ="""
    SELECT name from genres
    where GenreId = ?;
    """
    consulta2 = """
    SELECT t.name,g.name as Genero from tracks t
    JOIN albums a on t.AlbumId = a.AlbumId
    JOIN artists p on a.ArtistId = p.ArtistId
    JOIN genres g on t.GenreId = g.GenreId	
    WHERE g.GenreId = ?
    ORDER BY t.name ASC;
    """
    res =con.execute(consulta1,(id,))
    genero = res.fetchone()
    res =con.execute(consulta2,(id,))
    canciones = res.fetchall()

    pagina = render_template('detalle_genero.html',
    genero = genero,
    canciones = canciones)
    return pagina

