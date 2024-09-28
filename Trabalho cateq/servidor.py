from flask import Flask, render_template, request, jsonify, url_for, redirect
from datetime import datetime  # Importação necessária para data e hora
import qrcode
import os

app = Flask(__name__)

dados_armazenados = {}

@app.route('/')
def index():
    return render_template('index.html', qr_code_path=None)

@app.route('/gerar_qrcode', methods=['POST'])
def gerar_qrcode():
    mesa_id = request.form.get('mesa_id', type=int)
    if mesa_id:
        mesa_url = url_for('mostrar_cardapio', mesa_id=mesa_id, _external=True)
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(mesa_url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        qr_code_path = os.path.join('static', f'qrcode_mesa_{mesa_id}.png')
        img.save(qr_code_path)
        return render_template('index.html', qr_code_path=f'qrcode_mesa_{mesa_id}.png')

    return redirect(url_for('index'))

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

    dados_armazenados['dados'] = dados

    return jsonify(dados_armazenados['dados']), 200

@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify(dados_armazenados), 200

@app.route('/nota_fiscal')
def nota_fiscal():
    mesa_id = request.args.get("mesa_id")
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('nota_fiscal.html', dados=dados_armazenados.get('dados', {}), data_atual=data_atual, mesa_id = mesa_id)

if __name__ == "__main__":
    app.run(debug=True, port=3311)
