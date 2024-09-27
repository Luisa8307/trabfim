from flask import Flask, render_template, request, jsonify
from datetime import datetime  # Importação necessária para data e hora

app = Flask(__name__)

dados_armazenados = {}

@app.route("/mesa/<int:mesa_id>")
def mostrar_cardapio(mesa_id):
    return render_template("menu.html", mesa_id=mesa_id)

@app.route("/confirmacao")
def confirmacao_pedido():
    mesa_id = request.args.get("mesa_id")
    return render_template("confirmacao.html", mesa_id=mesa_id)

@app.route('/api/dados', methods=['POST'])
def api_dados():
    dados = request.json
    dados_armazenados['dados'] = dados.get('dados')
    return jsonify(dados), 200

@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify(dados_armazenados), 200

@app.route('/nota_fiscal')
def nota_fiscal():
    mesa_id = request.args.get('mesa_id')
    quantidade_hamb = int(request.args.get('quantidade_hamb', 0))
    quantidade_pizz = int(request.args.get('quantidade_pizz', 0))
    quantidade_suc = int(request.args.get('quantidade_suc', 0))

    total = (quantidade_hamb * 20) + (quantidade_pizz * 30) + (quantidade_suc * 5)
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return render_template('nota_fiscal.html', mesa_id=mesa_id, 
                           quantidade_hamb=quantidade_hamb, 
                           quantidade_pizz=quantidade_pizz, 
                           quantidade_suc=quantidade_suc, 
                           total=total,
                           data=data_atual)

if __name__ == "__main__":
    app.run(debug=True, port=3311)
