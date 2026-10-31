import random

from flask import Flask, render_template

app = Flask(__name__)


def area():
    """Cria o tabuleiro 8x8 com a cobra e uma maçã em posições livres."""
    tabuleiro = [["vazio" for _ in range(8)] for _ in range(8)]

    # Cada posição usa coordenadas (linha, coluna), começando em zero.
    posicoes_cobra = [(3, 3), (3, 2), (3, 1)]
    for indice, (linha, coluna) in enumerate(posicoes_cobra):
        tabuleiro[linha][coluna] = "cobra_cabeca" if indice == 0 else "cobra"

    posicoes_livres = [
        (linha, coluna)
        for linha in range(8)
        for coluna in range(8)
        if tabuleiro[linha][coluna] == "vazio"
    ]
    linha_maca, coluna_maca = random.choice(posicoes_livres)
    tabuleiro[linha_maca][coluna_maca] = "maca"

    return tabuleiro


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    return render_template("index.html", area=area())


if __name__ == "__main__":
    app.run(debug=True)
