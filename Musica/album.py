from flask import Blueprint, render_template
from . import db
bp = Blueprint('genero', __name__,url_prefix= '/genero')
@bp.route('/')
def albums():
    base_de_datos = db.get_db()
    consulta = """
        select title from albums
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
    #m falta cambiar esto
    #consulta2 = """
    #SELECT t.name,g.name as Genero, g.GenreId as idG from tracks t
    #JOIN albums a on t.AlbumId = a.AlbumId
    #JOIN artists p on a.ArtistId = p.ArtistId
    #JOIN genres g on t.GenreId = g.GenreId	
    #WHERE g.GenreId = ?
    #ORDER BY t.name ASC;
    #"""
    #res =con.execute(consulta1,(id,))
    #genero = res.fetchone()
    #res =con.execute(consulta2,(id,))
    #canciones = res.fetchall()

    #pagina = render_template('detalle_genero.html',
    #genero = genero,
    #canciones = canciones)
    #return pagina
