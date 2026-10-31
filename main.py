from flask import Flask, render_template

app = Flask(__name__)

def area():
    tabuleiro = [[]*8]*8
    cobra = {'tamanho': 3, 'posicao': [3,2,1]}

    import random
    maca = random.randint(1, 64)
    while(maca in cobra['posicao']):
        maca = random.randint(1, 64)

    for i in range(1, 65):
        if not i in cobra['posicao'] and i != maca:
            linha = i // 8
            coluna = i % 8
            tabuleiro[linha][coluna] = 'vazio'
        elif i != maca:
            if cobra['posicao'] != cobra['posicao'][0]
                tabuleiro[linha][coluna] = 'cobra'
            else:
                tabuleiro[linha][coluna] = 'cobra_cabeca'
        else:
            tabuleiro[linha][coluna] = 'maca'

        return tabuleiro

@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    return render_template("index.html", area=area())


if __name__ == "__main__":
    app.run(debug=True)
