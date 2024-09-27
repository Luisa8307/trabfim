from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dados_armazenados = {}

@app.route("/mesa/<int:mesa_id>")
def mostrar_cardapio(mesa_id):
    return render_template("menu.html", mesa_id=mesa_id)


@app.route("/confirmacao")
def confirmacao_pedido():
    mesa_id = request.args.get("mesa_id")
    return render_template("confirmacao.html", mesa_id=mesa_id,)


@app.route('/api/dados', methods=['POST'])
def api_dados():
    dados = request.json
    dados_armazenados['dados'] = dados.get('dados')

    return jsonify(dados), 200


@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify(dados_armazenados), 200

if __name__ == "__main__":
    app.run(debug=True, port=3311)
