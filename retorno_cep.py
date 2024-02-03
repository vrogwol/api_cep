from flask import Flask
import requests


def retorno_cep(self, cidade, logradouro, uf, bairro):

    retorno = """
        <html>
            <head>
            <style>
                p{float
                    font-size:20px;
                }
            </style>
            </head>
            <body>
                <p> Sua cidade é {cidade};</p>
                <br><br>
                <p> Seu logradoro é {logradouro};</p>
                <br><br>
                <p> Sua uf é {uf};</p>
                <br><br>
                <p> Seu bairro é {bairro};</p>
            <body>
        <html>
    """

    return retorno

def verifica_via_cep(cep_inserido):

    url = f'https://viacep.com.br/ws/{cep_inserido}/json/'
    response = requests.get(url)
    
    
    data = response.json()
    return data

