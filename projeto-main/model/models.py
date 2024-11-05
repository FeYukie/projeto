class Jogo:
    def __init__(self, cod, genero, nome, ano, preco):#nome
        self.cod=cod
        self.genero=genero
        self.ano=ano
        self.nome=nome
        self.preco=preco

carrinho_jogos=[]

def add_carrinho(jogo):
    cod = len(carrinho_jogos) + 1
    novo_jogo = Jogo(cod, jogo)
    carrinho_jogos.append(novo_jogo)



class User:
    def __init__(self, nome, tipo, senha):
        self.tipo=tipo
        self.senha=senha
        self.nome=nome

users=[]
users.append(User("Fernanda","Admin", "123"))
users.append(User("Mari", "Cliente", "1234"))

jogos=[]
jogos.append(Jogo(1, "Simulação",	"The Sims 4", "2014", 149))
jogos.append(Jogo(2,  "Cooperação",  "Overcooked!",  "2016",  "R$ 79"))
jogos.append(Jogo(3,  "Simulação",  "House Flipper",  "2018",  "R$ 99"))
jogos.append(Jogo( "4",  "Horror",  "Five Nights at Freddy's",  "2014",  "R$ 29"))
jogos.append(Jogo( "5",  "Sandbox",  "Minecraft",  "2011",  "R$ 89"))
jogos.append(Jogo( "6",  "Aventura",  "Little Nightmares",  "2017",  "R$ 49"))


def add_jogo(genero, nome, ano, preco):
    cod = len(jogos) + 1
    novo_jogo = Jogo(cod, genero, nome, ano, preco)
    jogos.append(novo_jogo)