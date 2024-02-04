"""
Este módulo fornece funções para consultar informações de endereço com base no CEP guardando em um banco de dados local todas as requisições que ja foram realizadas.

Necessário:
pip install flask
pip install requests

Inicie o servidor com o comando: flask run

"""



from flask import Flask, jsonify
from retorno_cep import verifica_via_cep, retorna_endereco
from dados import consulta_tabela, insert_cep

app = Flask(__name__)

@app.route("/")
def index():
    return "Insira o CEP desejado na URL :)",200   


@app.route("/<cep>/")
def cep_html(cep):
    if not cep.isdigit() or len(cep) != 8:
        return {'error': 'O CEP deve ser valido e sem hifen(-)'}, 400
    else:
        existe = consulta_tabela(cep)
        if existe:
            return retorna_endereco(existe, "html", "tupla"),200          
        else:
            resultado = verifica_via_cep(cep)
            insert_cep(resultado)

            return retorna_endereco(resultado),200    

@app.route("/<cep>/json/")
def cep_json(cep):
    if not cep.isdigit() or len(cep) != 8:
        return jsonify({'error': 'O CEP deve ser valido e sem hifen(-)'}), 400
    else:
        existe = consulta_tabela(cep)
        if existe:
            return retorna_endereco(existe,"json","tupla"),200        
        else:
            resultado = verifica_via_cep(cep)
            insert_cep(resultado)
            return retorna_endereco(resultado, "json"),200   


if __name__ == "__main__":
     app.run(debug=True)
