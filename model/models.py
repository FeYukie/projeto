class Jogo:
    def __init__(self, cod, tipo, jogo, ano):#nome
        self.cod=cod
        self.tipo=tipo
        self.ano=ano
        self.jogo=jogo
#self.nome=nome
carrinho_jogos=[]

def add_jogo(jogo):
    cod = len(carrinho_jogos) + 1
    novo_jogo = Jogo(cod, jogo)
    carrinho_jogos.append(novo_jogo)

class User:
    def __init__(self, nome, tipo, senha):
        self.tipo=tipo
        self.senha=senha
        self.nome=nome

users=[]