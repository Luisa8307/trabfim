from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/mesa/<int:mesa_id>")
def mostrar_cardapio(mesa_id):
    return render_template("menu.html", mesa_id=mesa_id)


@app.route("/confirmacao")
def confirmacao_pedido():
    mesa_id = request.args.get("mesa_id")
    return render_template("confirmacao.html", mesa_id=mesa_id,)


if __name__ == "__main__":
    app.run(debug=True, port=3311)
