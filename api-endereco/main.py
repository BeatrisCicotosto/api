import requests
import pandas as pd
from sqlalchemy import create_engine

lista_ceps: list = ['01153000', '20050000', '70714020']
lista_enderecos: list = []

for cep in lista_ceps:
    url: str = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        req = requests.get(url, timeout=3)
        if req.status_code == 200:
            endereco = req.json()
            lista_enderecos.append(
                            [
                                endereco['cep'],
                                endereco['logradouro'],
                                endereco['bairro'],
                                endereco['localidade'],
                                endereco['uf']
                            ]
                )
        else:
            erro = req.raise_for_status()
            print(f'Ocorreu o seguinte erro no acesso da API: {erro}')
    except Exception as erro:
        print(f'Ocorreu o seguinte erro na execução do código: {erro}')

for item in lista_enderecos:
    print(item)

df_enderecos = pd.DataFrame(
                lista_enderecos,
                columns=[
                            'cep',
                            'logradouro',
                            'bairro',
                            'localidade',
                            'uf'
                        ]
    )

db_connection = 'mysql+pymysql://root:@localhost:3306/endereco'
db_connection = create_engine(db_connection)
df_enderecos.to_sql(
                    con=db_connection,
                    name='enderecos',
                    if_exists='append',
                    index=False
    )
