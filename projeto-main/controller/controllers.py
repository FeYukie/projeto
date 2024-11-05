from flask import Blueprint, session, render_template, request, redirect,url_for, flash
from model.models import carrinho_jogos, users, jogos, User#,add_jogo

jogos_controller=Blueprint('jogo', __name__)

@jogos_controller.route('/')
def index():
    carrinho=session.get('carrinho',[])
    return render_template('index.html', jogos=jogos, carrinho=carrinho)

@jogos_controller.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        senha=request.form['senha']
        user_encontrado=None
        for user in users:
            if user.nome==username and user.senha==senha:
                user_encontrado=user
                break
            if user_encontrado:
                session['username'] = user_encontrado.nome
                flash(f"Boas-vindas, {user_encontrado.nome}!", "success")
                return redirect(url_for('jogo.index'))
            else:
                flash("Informações incorretas","error")
                return redirect(url_for("jogo.index"))
    return render_template('login.html')

@jogos_controller.route('/adicionar_ao_carrinho/<int:cod>', methods=['GET'])
def adicionar_ao_carrinho(cod):
    jogo_encontrado=None
    for jogo in jogos:
        if jogo.cod == cod:
            jogo_encontrado = jogo
            break
    if jogo_encontrado:
        if 'carrinho' not in session:
            session['carrinho'] = []  
        session['carrinho'].append(jogo_encontrado.nome)  
        flash(f"Você adicionou {jogo_encontrado.nome} ao seu carrinho!", "success")
    else:
        flash("Jogo não encontrado!", "error")

    return redirect(url_for('jogo.index')) 


@jogos_controller.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('jogo.index'))

if __name__=='__main__':
    jogos_controller.run(debug=True)