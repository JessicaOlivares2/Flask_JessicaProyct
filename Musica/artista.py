from flask import Blueprint, render_template,request,redirect,url_for
from . import db
bp = Blueprint('artista', __name__,url_prefix= '/artista')
@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
        select name,ArtistId from artists
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("artista.html",artistas=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 ="""
    select name,ArtistId from artists
    where ArtistId = ?;
    """
    
    consulta2 = """
    select a.ArtistId,name,b.Title as titulo,b.AlbumId from artists a
    left join albums b on a.ArtistId = b.ArtistId
    WHERE a.ArtistId = ? 
    AND AlbumId is not NULL
    ORDER BY name ASC;
    """
    
    res =con.execute(consulta1,(id,))
    artista= res.fetchone()
    res =con.execute(consulta2,(id,))
    albums = res.fetchall()

    pagina = render_template('detalle_artista.html',
    artista = artista,
    albums = albums)
    return pagina

@bp.route('/new', methods =('GET', 'POST'))
def nuevo():
   if request.method == 'POST':
       name = request.form['name']
       con = db.get_db()
       consulta = """
               INSERT INTO artists(name)
               VALUES(?)
           """
       con.execute(consulta, (name,))
       con.commit()
       return redirect(url_for('artista.artistas'))
   else:
       pagina = render_template('nuevo_artista.html',)
       return pagina


