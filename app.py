import flask
from alergias import alergias
from clientes import clientes
from consumos import consumos
from datas import datas
from ementas import ementas
from funcionarios import funcionarios
from itens import itens
from locaisConsumo import locaisConsumo
from locais import locais
from restaurantes import restaurantes
from tiposEmenta import tiposEmenta
from tiposItens import tiposItens
from tiposRefeicao import tiposRefeicao


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(alergias)
app.register_blueprint(clientes)
app.register_blueprint(consumos)
app.register_blueprint(datas)
app.register_blueprint(ementas)
app.register_blueprint(funcionarios)
app.register_blueprint(itens)
app.register_blueprint(locaisConsumo)
app.register_blueprint(locais)
app.register_blueprint(restaurantes)
app.register_blueprint(tiposEmenta)
app.register_blueprint(tiposItens)
app.register_blueprint(tiposRefeicao)

app.run()
