from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html', resultado=None)

@app.route('/emprestimo', methods=['POST'])
def emprestimo():
    try:
        valor   = float(request.form['casa'])
        salario = float(request.form['salario'])
        tempo   = float(request.form['tempo'])

        mensalidade = valor / (tempo * 12) # Mensalidade do empréstimo
        limite      = salario * 0.3        # 30% do salário

        if mensalidade > limite:
            resultado = "Empréstimo negado: parcela ultrapassa 30% do salário."
        else:
            resultado = f"Empréstimo aprovado! Parcela: R$ {mensalidade:.2f}"

        return render_template('index.html', resultado=resultado)
    except:
        return render_template('index.html', resultado="Erro ao processar os dados.")
