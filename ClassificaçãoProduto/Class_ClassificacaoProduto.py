from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from DataBase import DataBase
import sqlite3


class Classificao_Produto(DataBase.Model):

  __tablename__ = 'classificacaoProduto'
  id = DataBase.Column(DataBase.Integer, primary_key=True)
  Descricao = DataBase.Column(DataBase.String(80), nullable=False)
  
  conn = sqlite3.connect("classificacaoProduto.db")
  
  '''
  def db() -> sqlite3.Connection:
    db = sqlite3.connect(db_file)
    yield db
    db.close()
  '''
  
  def __init__(self, Descricao):
    self.Descricao = Descricao

  def __repr__(self):
    return f"Descricao: {self.Descricao}"