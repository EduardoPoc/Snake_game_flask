from flask import Flask, render_template

app = Flask(__name__)


def quadriculado():
    """Retorna as 36 posições do tabuleiro."""
    return range(36)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/jogar")
def jogar():
    return render_template("index.html", area=quadriculado())


if __name__ == "__main__":
    app.run(debug=True)
