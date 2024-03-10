from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar-requisicao', methods=['POST'])
def processar_requisicao():
    data = request.get_json()
    print(data)

    # Realize o processamento necessário com os dados recebidos
    key_from_client = data.get('key', '')
    resposta_do_servidor = f"Você enviou: {key_from_client}"
    print(key_from_client)

    return jsonify(resposta_do_servidor)

if __name__ == '__main__':
    app.run(debug=True)
