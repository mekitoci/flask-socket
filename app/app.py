from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("client_connect")
def handle_connect(message):
    try:
        emit("response", {"data": "Server: Connect to Server!"})
    except Exception as e:
        emit("response", {"data": str(e)})


@socketio.on("client_message")
def handle_message(message):
    try:
        emit("response", {"data": "Server: Mic Test123"})
    except Exception as e:
        emit("response", {"data": str(e)})


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True,pingInterval = 10000, pingTimeout= 5000)
