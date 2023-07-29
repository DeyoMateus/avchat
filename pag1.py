# Importando recursos
#Estrutura padrão "!" html
#websocket html
#https://cdnjs.com/ (socket.io, jquery)
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins = "*")

#Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast = True)

# Primeira pag = 1ª rota
@app.route("/")
def homepage():
    return render_template("visual.html")
    

# Roda o app
socketio.run(app, host = "192.168.2.115") 



