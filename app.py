from flask import Flask, request, jsonify, render_template
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar', methods=['POST'])
def criar():
    dados = request.json
    parametros = dados.get('parametros', {})
    if(criarInstancia(**parametros)):
        return jsonify({'resultado':'Usuário Cadastrado'})
    
@app.route('/remover', methods=['POST'])
def remover():
    dados = request.json
    parametros = dados.get('parametros', {})
    if(removerInstancia(**parametros)):
        return jsonify({'resultado':'Usuário Removido'})



# @app.route('/executar-funcao', methods=['POST'])
# def executar_funcao():
#     dados = request.json
#     nome_funcao = dados.get('funcao')
#     parametros = dados.get('parametros', {})

#     if nome_funcao:
#         if nome_funcao == 'criarInstancia':
#             resultado = criarInstancia(**parametros)
#         elif nome_funcao == 'removerInstancia':
#             resultado = removerInstancia(**parametros)
#         else:
#             return jsonify({'erro': 'Função não encontrada'}), 404

#         return jsonify({'resultado': resultado})
#     else:
#         return jsonify({'erro': 'Nome da função não especificado'}), 400


if __name__ == '_main_':
    app.run(debug=True)
