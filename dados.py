import sqlite3
# conect = sqlite3.connect('cep_registro.db')
# cursor = conect.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS CEPS_CONSULTADOS (
#         cep TEXT PRIMARY KEY,
#         cidade TEXT,
#         logradouro TEXT,
#         uf TEXT,
#         bairro TEXT
#     )
# ''')
# conect.commit()
# conect.close()

def consulta_tabela(cep):
    conect = sqlite3.connect('cep_registro.db')
    cursor = conect.cursor()
    cursor.execute(f'''
        SELECT * FROM CEPS_CONSULTADOS WHERE cep = "{cep}"                                  
    ''')

    resultado = cursor.fetchone()
    conect.commit()
    conect.close()

    
    return resultado


def insert_cep(endereco):
    
    
    cep = endereco["cep"].replace("-", "")
    cidade_cep = endereco["localidade"]
    logradouro_cep = endereco["logradouro"]
    uf_cep = endereco["uf"]
    bairro_cep = endereco["bairro"]
    conect = sqlite3.connect('cep_registro.db')
    cursor = conect.cursor()
    cursor.execute(f'''
        INSERT INTO CEPS_CONSULTADOS (cep, cidade, logradouro, uf, bairro)
        VALUES ("{cep}","{cidade_cep}", "{logradouro_cep}", "{uf_cep}", "{bairro_cep}")
    '''
    )
    conect.commit()
    conect.close()
    return

