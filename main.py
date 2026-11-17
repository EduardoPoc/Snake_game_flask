from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

intervalo = 3.0
proxima_execucao = time.monotonic() + intervalo

direcoes = {
    'up': [0, -1],
    'down': [0, 1],
    'left': [-1, 0],
    'right': [1, 0]
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


def area(cobra=None):
    tabuleiro = [['vazio' for _ in range(8)] for _ in range(8)]
    if None == cobra:
        cobra = cobraInicial
    
    maca = Item(random.randint(0, 7), random.randint(0, 7))

    while(maca.getPosition() in [i.getPosition() for i in cobra]):
        maca = Item(random.randint(0, 7), random.randint(0, 7))

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

    cobra.insert(Item(x, y))

    cobra.pop()
    return cobra

def rodar(direcao, proxima_execucao):
    espera = proxima_execucao - time.monotonic()

    if espera > 0:
        time.sleep(espera)

    if cobra:
        cobra = andarCobra(cobra, direcao)
        jogar(area())


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar(area=None):
    if area:
        return render_template("index.html", area=area)
    
    return render_template("index.html", area=area())

@app.post("/tecla")
def receber_tecla():
    dados = request.get_json()
    direcao = dados.get("direcao")

    rodar(direcao)

if __name__ == "__main__":
    app.run(debug=True)
