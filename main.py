from flask import Flask, render_template

app = Flask(__name__)


def criar_area(linhas=6, colunas=6):
    """Cria uma matriz bidimensional com as posições vazias do tabuleiro."""
    return [[0 for _ in range(colunas)] for _ in range(linhas)]


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    matriz = criar_area()
    return render_template("index.html", area=matriz)


if __name__ == "__main__":
    app.run(debug=True)
