from flask import Flask, render_template
import random

app = Flask(__name__)

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

@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    return render_template("index.html", area=area())


if __name__ == "__main__":
    app.run(debug=True)
