from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from DataBase import DataBase
import sqlite3

class Cliente(DataBase.Model):
  __tablename__ = 'Cliente'
  id = DataBase.Column(DataBase.Integer, primary_key=True)
  Nome = DataBase.Column(DataBase.String(70))
  Telefone = DataBase.Column(DataBase.String(50))
  Logradouro = DataBase.Column(DataBase.String(100))
  Numero = DataBase.Column(DataBase.String(50))
  Complemento	= DataBase.Column(DataBase.String(50))
  Bairro = DataBase.Column(DataBase.String(50))
  Cidade = DataBase.Column(DataBase.String(50))
  UF = DataBase.Column(DataBase.String(100))
  Senha = DataBase.Column(DataBase.String(100))

  def __init__(self, Nome, Telefone, Logradouro, Numero, Complemento, Bairro, Cidade, UF, Senha):
    self.Nome = Nome
    self.Telefone = Telefone
    self.Logradouro = Logradouro
    self.Numero = Numero
    self.Complemento = Complemento
    self.Bairro = Bairro
    self.Cidade = Cidade
    self.UF = UF
    self.Senha = Senha

def __repr__(self):
  return f"Cliente: {self.Nome}"