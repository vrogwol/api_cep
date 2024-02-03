from flask import Flask
from retorno_cep import verifica_via_cep


app = Flask(__name__)

@app.route("/")
def index():
    return "Insira o CEP desejado na URL :)"


@app.route("/<int:cep>/")
def consulta_cep(cep):

    print (verifica_via_cep(cep))


    return "ba"



