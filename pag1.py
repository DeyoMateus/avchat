# Importando recursos
#Estrutura padrão "!" html
#websocket html
#https://cdnjs.com/ (socket.io, jquery)
from flask import Flask, render_template

app = Flask(__name__)

# Primeira pag = 1ª rota
@app.route("/")
def homepage():
    return render_template("homepage.html")
    

# Roda o app
app.run()



