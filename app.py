from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)

CAMINHO_PROJETOS = 'data/projetos.csv'
CAMINHO_TAREFAS = 'data/tarefas.csv'


def carregar_projetos():
    projetos = []
    if os.path.exists(CAMINHO_PROJETOS):
        with open(CAMINHO_PROJETOS, newline='', encoding='utf-8') as f:
            for linha in csv.DictReader(f):
                projetos.append(linha)
    return projetos


def salvar_projetos(projetos):
    with open(CAMINHO_PROJETOS, 'w', newline='', encoding='utf-8') as f:
        campos = ['id', 'nome', 'descricao', 'data_criacao']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(projetos)


def carregar_tarefas():
    tarefas = []
    if os.path.exists(CAMINHO_TAREFAS):
        with open(CAMINHO_TAREFAS, newline='', encoding='utf-8') as f:
            for linha in csv.DictReader(f):
                tarefas.append(linha)
    return tarefas


def salvar_tarefas(tarefas):
    with open(CAMINHO_TAREFAS, 'w', newline='', encoding='utf-8') as f:
        campos = ['id', 'projeto_id', 'titulo', 'descricao', 'status']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(tarefas)


@app.route('/')
def index():
    projetos = carregar_projetos()
    return render_template('index.html', projetos=projetos)


@app.route('/criar', methods=['GET', 'POST'])
def criar_projeto():
    if request.method == 'POST':
        projetos = carregar_projetos()
        novo = {
            'id': str(len(projetos) + 1),
            'nome': request.form['nome'],
            'descricao': request.form['descricao'],
            'data_criacao': datetime.today().strftime('%Y-%m-%d')
        }
        projetos.append(novo)
        salvar_projetos(projetos)
        return redirect(url_for('index'))
    return render_template('criar_projeto.html')


@app.route('/projeto/<id>')
def ver_projeto(id):
    projetos = carregar_projetos()
    projeto = None
    for p in projetos:
        if p['id'] == id:
            projeto = p
            break
    tarefas = [t for t in carregar_tarefas() if t['projeto_id'] == id]
    return render_template('projeto.html', projeto=projeto, tarefas=tarefas)


@app.route('/projeto/<id>/excluir')
def excluir_projeto(id):
    projetos = carregar_projetos()
    tarefas = carregar_tarefas()
    projetos = [p for p in projetos if p['id'] != id]
    tarefas = [t for t in tarefas if t['projeto_id'] != id]
    salvar_projetos(projetos)
    salvar_tarefas(tarefas)
    return redirect(url_for('index'))


@app.route('/projeto/<id>/editar', methods=['GET', 'POST'])
def editar_projeto(id):
    projetos = carregar_projetos()
    projeto = None
    for p in projetos:
        if p['id'] == id:
            projeto = p
            break

    if request.method == 'POST' and projeto:
        projeto['nome'] = request.form['nome']
        projeto['descricao'] = request.form['descricao']
        salvar_projetos(projetos)
        return redirect(url_for('index'))

    return render_template('editar_projeto.html', projeto=projeto)


@app.route('/adicionar_tarefa/<projeto_id>', methods=['POST'])
def adicionar_tarefa(projeto_id):
    tarefas = carregar_tarefas()
    nova = {
        'id': str(len(tarefas) + 1),
        'projeto_id': projeto_id,
        'titulo': request.form['titulo'],
        'descricao': request.form['descricao'],
        'status': request.form['status']
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    return redirect(url_for('ver_projeto', id=projeto_id))


@app.route('/editar_tarefa/<id>/<projeto_id>', methods=['POST'])
def editar_tarefa(id, projeto_id):
    tarefas = carregar_tarefas()
    tarefa = None
    for t in tarefas:
        if t['id'] == id:
            tarefa = t
            break

    if tarefa:
        tarefa['titulo'] = request.form['titulo']
        tarefa['descricao'] = request.form['descricao']
        tarefa['status'] = request.form['status']
        salvar_tarefas(tarefas)

    return redirect(url_for('ver_projeto', id=projeto_id))


@app.route('/remover_tarefa/<id>/<projeto_id>')
def remover_tarefa(id, projeto_id):
    tarefas = carregar_tarefas()
    tarefas = [t for t in tarefas if t['id'] != id]
    salvar_tarefas(tarefas)
    return redirect(url_for('ver_projeto', id=projeto_id))


if __name__ == '__main__':
    app.run(debug=True)