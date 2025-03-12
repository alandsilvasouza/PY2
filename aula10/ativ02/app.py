# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import hashlib

app = Flask(__name__)
app.secret_key = 'alasjmska'  # Necessário para sessões e mensagens flash

# Usuário mockado para exemplo (em produção use banco de dados)
def carregar_usuarios():
    with open('usuarios.json', 'r') as file:
        return json.load(file)
    
def verificar_senha(usuario, senha):
    usuarios = carregar_usuarios()
    if usuario in usuarios:
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        return hash_senha == usuarios[usuario]
    return False


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if verificar_senha(usuario, senha):
            session['usuario_logado'] = usuario
            return redirect(url_for('sucesso'))
        else:
            flash('Credenciais inválidas. Tente novamente!', 'error')
    
    return render_template('login.html')

@app.route('/sucesso')
def sucesso():
    if 'usuario_logado' in session:
        return render_template('sucesso.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)