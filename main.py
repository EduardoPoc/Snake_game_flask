from flask import Flask, render_template

app = Flask(__name__)

def quadriculado():
    return "algo" * 36

@app.route("/")
def index():
    return render_template("base.html")

@app.route('/jogar')
def jogar():
    tabela = quadriculado()
    return render_template("index.html", area=tabela)


if __name__ == "__main__":
    app.run(debug=True)
