from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chavesecreta'
usuarios = {'admin': 'senha123', 'leandro': 'soubonito', 'william': 'reidelas'}

# Página inicial - usuário logado
@app.route('/')
def inicio():
    if 'usuario' in session:
        return redirect(url_for('escolher_sala'))  # Redireciona para a escolha da sala
    else:
        return redirect(url_for('login'))

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Credenciais inválidas. Por favor, tente novamente.', 'danger')
    
    return render_template('login.html')

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login'))

# Página de escolha da sala
@app.route('/escolher_sala', methods=['GET', 'POST'])
def escolher_sala():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        sala = request.form['sala']
        flash(f'Sala {sala} escolhida!', 'success')
        return redirect(url_for('agendar', sala=sala))

    return render_template('escolher_sala.html')

# Página de agendamento
@app.route('/agendar/<sala>', methods=['GET', 'POST'])
def agendar(sala):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        horario = request.form['horario']
        flash(f'Horário {horario} agendado para a {sala}.', 'success')
        return redirect(url_for('inicio'))

    return render_template('agendar.html', sala=sala)

# Execução do aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
