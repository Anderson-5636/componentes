from flask import Flask
from DataBase import DataBase
from flask_migrate import Migrate
from Route_ClassificacaoProduto import bp_classificacaoProduto

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'SECRETO'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATION'] = False

app.register_blueprint(bp_classificacaoProduto, url_prefix='/classificacaoProduto')

migrate = Migrate(app, DataBase)
DataBase.init_app(app)

@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)


