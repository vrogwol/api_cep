import requests
from flask import jsonify


def verifica_via_cep(cep_inserido):
    url = f'https://viacep.com.br/ws/{cep_inserido}/json/'
    response = requests.get(url)
    
    data = response.json()

    return data

def retorna_endereco(endereco, retorno="html", formato="outro"):
    if retorno == "json":
        return jsonify(endereco)
    else:
        if formato == "tupla":
            cep, cidade, logradouro, uf, bairro = endereco
        else:
            
            cep = endereco['cep']
            cidade = endereco['localidade']
            logradouro = endereco['logradouro']
            uf = endereco['uf']
            bairro = endereco['bairro']

        retorno = f"""
            <html>
                <head>
                    <title>Consulta Cep</title>
                </head>
                <body>
                    <p> Sua cidade é <span style="color:red;font-size:2em;"> {cidade}</span>;</p>
                    <br>
                    <p> Seu logradoro é <span style="color:red;font-size:2em;"> {logradouro}</span>;</p>
                    <br>
                    <p> Sua uf é <span style="color:red;font-size:2em;"> {uf}</span>;</p>
                    <br>
                    <p> Seu bairro é <span style="color:red;font-size:2em;"> {bairro}</span>;</p>
                <body>
            <html>
        """
        return retorno