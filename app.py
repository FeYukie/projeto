from flask import Flask, session, redirect, url_for, request, render_template
from controller.controllers import jogos_controller
#from model.models import jogos,add_jogo
#from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(jogos_controller)
app.secret_key='log123'



if __name__=='__main__':
    app.run(debug=True)