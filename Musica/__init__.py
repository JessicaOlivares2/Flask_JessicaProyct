from flask import Flask, render_template

app = Flask(__name__)#le dice donde esta ubicado la app

with app.app_context() :
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'


#importamos y registramos el blueprint 
from . import genero
app.register_blueprint(genero.bp)
from . import artista
app.register_blueprint(artista.bp)
from . import album
app.register_blueprint(album.bp)
from . import tracks
app.register_blueprint(tracks.bp)