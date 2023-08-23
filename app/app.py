from flask import Flask, request, render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/inserir-livro.html')
def inserir():
    return render_template('inserir-livro.html')

@app.route('/cadastro', methods=['POST'])
def olá():
    name = request.form['name']
    genero = request.form['genero']
    valor = request.form['valor']

    return render_template('/feedback.html',nome=name,genero=genero,valor=valor)
    


if __name__ == '__main__':
    app.run(debug=True)