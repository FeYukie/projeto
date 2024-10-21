from flask import Blueprint, session, render_template, request, redirect,url_for
from model.models import carrinho_jogos#,add_jogo

jogos_controller=Blueprint('jogo', __name__)
#@jogos_controller.route('/')
#def index():
    #return render_template('index.html', jogos=jogos)
@jogos_controller.route('/')
def index():
    if 'username' in session:
        return f'Olá, {session["username"]}!'
    return 'Sem login!'

@jogos_controller.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('jogo.index'))
    return render_template('index.html')
    #if
    #salvar a lista dos produtos do carrinho nos cookies
    #erros do login no flash messages
    #cookies, middleware
    #500,404,403

@jogos_controller.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__=='__main__':
    jogos_controller.run(debug=True)