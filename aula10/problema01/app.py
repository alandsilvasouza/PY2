from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá, Mundo!'

@app.route('/oiee/<aluno>')
def oiee_aluno(aluno):
    return f'Boa noite {aluno}, se está vendo isso sua rota funcionou corretamente'


if __name__ == '__main__':
    app.run(debug=True)

