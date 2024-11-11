from flask import Flask, session, flash, redirect, url_for, request, render_template, make_response
from controller.controllers import jogos_controller
from model.models import users, User, add_jogo, jogos
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(jogos_controller)
app.secret_key='log123'

app.config['SESSION_COOKIE_SECURE']=True
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=4)

def verifica_login(f):
    def decorated(*args, **kwargs):
        if 'username' not in session:
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('jogo.login')) 
        return f(*args, **kwargs)
    return decorated

@app.route('/submit', methods=['POST'])
def submit():
    flash('Erro no login', 'error')
    return redirect(url_for('index'))

@app.route('/set_cookie')
def set_cookie():
    resp=make_response()
    resp.set_cookie('carrinho', 'carrinho_jogos[]', max_age=60*60*24)
    return resp

@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500



@app.route('/admin', methods=['POST','GET'])
@verifica_login
def admin():
    if request.method=='POST':
        genero = request.form.get('genero')
        nome = request.form.get('nome')
        ano = request.form.get('ano')
        preco = request.form.get('preco')
        if 'username' in session:
            for user in users:
                if user.tipo=='Admin':
                    add_jogo(genero, nome, ano, preco)
                    flash(f"Boas-vindas, {user.tipo}!", "success")
                    return redirect(url_for('jogo.admin'))        
                else:
                    flash("Acesso negado!","error")
                    return redirect(url_for("jogo.index"))
    return render_template('admin.html', jogos=jogos)


@app.route('/<int:cod>', methods=['PUT'])
def mudar(cod):
    teste = jogos[cod]
    novo = request
    teste.update(novo)
    return teste

@app.route('/<int:cod>', methods=['DELETE'])
def limpar(cod):
    teste = jogos[cod]
    if teste:
        jogos.remove(teste)

if __name__=='__main__':
    app.run(debug=True)