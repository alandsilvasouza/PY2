# Importações necessárias
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Configuração do aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --------------------------------------------
# Modelo do Banco de Dados
# --------------------------------------------

class Contato(db.Model):
    """Modelo para representar um contato na agenda"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<Contato {self.nome}>'

# --------------------------------------------
# Rotas do Flask
# --------------------------------------------

@app.route('/')
def index():
    """Página principal - lista todos os contatos"""
    termo_busca = request.args.get('busca', '')  # Pega o termo de busca da URL
    
    if termo_busca:
        # Filtra contatos que contenham o termo no nome
        contatos = Contato.query.filter(Contato.nome.ilike(f'%{termo_busca}%')).all()
    else:
        contatos = Contato.query.all()
    
    return render_template('index.html', contatos=contatos, termo_busca=termo_busca)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_contato():
    """Adiciona um novo contato à agenda"""
    if request.method == 'POST':
        # Cria novo contato com dados do formulário
        novo_contato = Contato(
            nome=request.form['nome'],
            telefone=request.form['telefone'],
            email=request.form['email']
        )
        db.session.add(novo_contato)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('formulario.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_contato(id):
    """Edita um contato existente"""
    contato = Contato.query.get_or_404(id)
    
    if request.method == 'POST':
        # Atualiza os dados do contato
        contato.nome = request.form['nome']
        contato.telefone = request.form['telefone']
        contato.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('formulario.html', contato=contato)

@app.route('/excluir/<int:id>')
def excluir_contato(id):
    """Exclui um contato da agenda"""
    contato = Contato.query.get_or_404(id)
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('index'))

# --------------------------------------------
# Execução do Aplicativo
# --------------------------------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria tabelas se não existirem
        
        # Adiciona contatos iniciais para teste
        if not Contato.query.first():
            contatos_iniciais = [
                Contato(nome='Prof. Daniel Mesquita', telefone='(45) 98431-8261', email='danielme17@gmail.com'),
            ]
            db.session.add_all(contatos_iniciais)
            db.session.commit()
    
    app.run(debug=True)