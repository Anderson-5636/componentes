# importando o Blueprint para ver as rotas
from flask import Blueprint, request, redirect, render_template
from Class_Cliente import Cliente
from DataBase import DataBase

bp_cliente = Blueprint('cliente', __name__, template_folder='templats')

#adicionando rota para os templates
@bp_cliente.route("/create", methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('Create_Cliente.html')
  elif request.method == 'POST':

    Nome = request.form['Nome']
    Telefone = request.form['Telefone']
    Logradouro = request.form['Logradouro']
    Numero = request.form['Numero']
    Complemento = request.form['Complemento']
    Bairro = request.form['Bairro']
    Cidade = request.form['Cidade']
    UF = request.form['UF']
    Senha = request.form['Senha']

    cliente = Cliente(Nome, Telefone, Logradouro, Numero, Complemento, Bairro,
                      Cidade, UF, Senha)
    DataBase.session.add(cliente)
    DataBase.session.commit()
    return 'Dados cadastrado com sucesso!'


@bp_cliente.route('/list')
def List():

  cliente = Cliente.query.all()
  return render_template('List_Cliente.html', cliente=cliente)


@bp_cliente.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

  cliente = Cliente.query.get(id)

  if request.method == 'GET':
    return render_template('Update_Cliente.html', cliente=cliente)

  elif request.method == 'POST':
    Nome = request.form['Nome']
    Telefone = request.form['Telefone']
    Logradouro = request.form['Logradouro']
    Numero = request.form['Numero']
    Complemento = request.form['Complemento']
    Bairro = request.form['Bairro']
    Cidade = request.form['Cidade']
    UF = request.form['UF']
    Senha = request.form['Senha']

    cliente.Nome = Nome
    cliente.Telefone = Telefone
    cliente.Logradouro = Logradouro
    cliente.Numero = Numero
    cliente.Complemento = Complemento
    cliente.Bairro = Bairro
    cliente.Cidade = Cidade
    cliente.UF = UF
    cliente.Senha = Senha

    DataBase.session.commit()
    return redirect('/cliente/list')


@bp_cliente.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  cliente = Cliente.query.get(id)
  if request.method == 'GET':
    return render_template('Delete_Cliente.html', cliente=cliente)

  elif request.method == 'POST':
    DataBase.session.delete(cliente)
    DataBase.session.commit()
    return redirect('/cliente/list')
