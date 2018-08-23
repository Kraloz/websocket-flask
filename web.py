# -*- coding: utf-8 -*-

# -Librería de eventos-
import eventlet
eventlet.monkey_patch()
# ---------------------
#   -Webserver-
from flask import Flask, render_template
# ---------------------
# -Extensión para flask de la SocketIO APi-
from flask_socketio import SocketIO, emit
# ---------------------
from settings import ASYNC_MODE


__author__ = 'Tomás Aprile'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app, async_mode=ASYNC_MODE)


@app.route("/")
def index():
    return render_template("index.html", title="Titulo", nombre="Kraloz")

# Escucha al evento connect de cualquier usuario (no estamos usando namespaces)
@socketio.on('connect')
def test_connect():
    print('Client connected')
    msg = "Hola!"
    # Emite un mensaje con el evento saludos al cliente/clientes
    # también envía un objeto que js va a poder levantar y acceder de una
    socketio.emit('saludo', {'msg': msg})

# Inicialicamos el servidor
if __name__ == '__main__':   
    socketio.run(app)
