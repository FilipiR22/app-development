from flask import Flask, request, jsonify, render_template
from functions. import *

app = Flask(_name_)

@app.route('/executar-funcao', methods=['POST'])
def executar_funcao():
    dados = request.json
    nome_funcao = dados.get('funcao')
    parametros = dados.get('parametros', {})

    if nome_funcao:
        if nome_funcao == 'funcao1':
            resultado = funcao1(**parametros)
        elif nome_funcao == 'funcao2':
            resultado = funcao2(**parametros)
        else:
            return jsonify({'erro': 'Função não encontrada'}), 404

        return jsonify({'resultado': resultado})
    else:
        return jsonify({'erro': 'Nome da função não especificado'}), 400


if _name_ == '_main_':
    app.run(debug=True)
