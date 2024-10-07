from flask import Blueprint, session, render_template, request, redirect,url_for
from model.models import jogos,add_jogo
from datetime import timedelta
jogos_controller=Blueprint('jogo', __name__)
#@jogos_controller.route('/')
#def index():
    #return render_template('index.html', jogos=jogos)
@jogos.controller.route('/')
def index():
    if 'username' in session:
        return f'Olá, {session["username"]}!'
    return 'Sem login!'

jogos.controller.config['SESSION_COOKIE_SECURE']=True
jogos.controller.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=4)
@jogos.controller.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Usuário: <input type="text" name="username">
            Senha: <input type="password" name="senha">
            <input type="submit" value="Enviar">
        </form>
    '''
    if
@jogos.controller.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))