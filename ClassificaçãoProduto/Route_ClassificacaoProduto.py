# importando o Blueprint para ver as rotas
from flask import Blueprint, request, redirect, render_template
from Class_ClassificacaoProduto import Classificao_Produto
from DataBase import DataBase

bp_classificacaoProduto = Blueprint('classificacaoProduto', __name__, template_folder='templats')


#adicionando rota para os templates
@bp_classificacaoProduto.route("/create", methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('Create_ClassificacaoProduto.html')
  elif request.method == 'POST':

    Descricao = request.form['Descricao']

    classificacaoProduto = Classificao_Produto(Descricao)
    DataBase.session.add(classificacaoProduto)
    DataBase.session.commit()
    return 'Dados cadastrado com sucesso!'


@bp_classificacaoProduto.route('/list')
def List():

  classificacaoProduto = Classificao_Produto.query.all()
  return render_template('List_ClassificacaoProduto.html', classificacaoProduto = classificacaoProduto)

@bp_classificacaoProduto.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

  classificacaoProduto = Classificao_Produto.query.get(id)

  if request.method == 'GET':
    return render_template('Update_ClassificacaoProduto.html', classificacaoProduto = classificacaoProduto)

  elif request.method == 'POST':
    Descricao = request.form['Descricao']

    classificacaoProduto.Descricao = Descricao
    DataBase.session.commit()
    return redirect('/classificacaoProduto/list')


@bp_classificacaoProduto.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  classificacaoProduto = Classificao_Produto.query.get(id)
  if request.method == 'GET':
    return render_template('Delete_ClassificacaoProduto.html', classificacaoProduto = classificacaoProduto)

  elif request.method == 'POST':
    DataBase.session.delete(classificacaoProduto)
    DataBase.session.commit()
    return redirect('/classificacaoProduto/list')
