from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

intervalo = 3.0
proxima_execucao = time.monotonic() + intervalo

direcoes = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}

class Item :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self.x, self.y
    
    
cobraInicial = [Item(3, 3), Item(3, 2), Item(3, 1)]
cobra = cobraInicial[:]
maca = Item(5, 5)
jogo_encerrado = False


def area(cobra=None):
    tabuleiro = [['vazio' for _ in range(8)] for _ in range(8)]
    if cobra is None:
        cobra = globals()['cobra']

    cabeca = cobra[0]
    tabuleiro[cabeca.x][cabeca.y] = 'cabeca_cobra'

    for parte in cobra[1:]:
        tabuleiro[parte.x][parte.y] = 'corpo_cobra'

    tabuleiro[maca.x][maca.y] = 'maca'
    
    return tabuleiro

def andarCobra(cobra, direcao=None):
    if direcao:
        x = cobra[0].x + direcoes[direcao][0]
        y = cobra[0].y + direcoes[direcao][1]
    else:
        x = cobra[0].x - cobra[1].x
        y = cobra[0].y - cobra[1].y
    
        x = cobra[0].x + x
        y = cobra[0].y + y

    cobra.insert(0, Item(x, y))

    cobra.pop()
    return cobra

def rodar(direcao):
    global cobra, maca, jogo_encerrado
    if jogo_encerrado:
        return cobra

    proxima_cobra = andarCobra(cobra[:], direcao)
    cabeca = proxima_cobra[0].getPosition()
    if (cabeca[0] < 0 or cabeca[0] >= 8 or cabeca[1] < 0 or cabeca[1] >= 8
            or cabeca in [parte.getPosition() for parte in cobra]):
        jogo_encerrado = True
        return cobra

    if proxima_cobra[0].getPosition() == maca.getPosition():
        proxima_cobra.append(cobra[-1])
        posicoes_livres = [(x, y) for x in range(8) for y in range(8)
                            if (x, y) not in [parte.getPosition() for parte in proxima_cobra]]
        if posicoes_livres:
            x, y = random.choice(posicoes_livres)
            maca = Item(x, y)
    cobra = proxima_cobra
    return cobra


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    global cobra, maca, jogo_encerrado
    cobra = [Item(3, 3), Item(3, 2), Item(3, 1)]
    maca = Item(5, 5)
    jogo_encerrado = False
    return render_template("index.html", area=area())

@app.post("/tecla")
def receber_tecla():
    dados = request.get_json(silent=True) or {}
    direcao = dados.get("direcao")
    if direcao not in direcoes:
        return jsonify({"erro": "Direção inválida"}), 400
    rodar(direcao)
    return jsonify({"area": area(), "fim": jogo_encerrado})

if __name__ == "__main__":
    app.run(debug=True)
