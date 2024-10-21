from flask import Flask, session, flash, redirect, url_for, request, render_template, make_response
from controller.controllers import jogos_controller
#from model.models import jogos,add_jogo
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(jogos_controller)
app.secret_key='log123'

app.config['SESSION_COOKIE_SECURE']=True
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=4)

@app.route('/submit', methods=['POST'])
def submit():
    flash('Erro no login', 'error')
    return redirect(url_for('index'))

@app.route('/set_cookie')
def set_cookie():
    resp=make_response()
    resp.set_cookie('carrinho', 'carrinho_jogos[]', max_age=60*60*24)
    return resp

if __name__=='__main__':
    app.run(debug=True)