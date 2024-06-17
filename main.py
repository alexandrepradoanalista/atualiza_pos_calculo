from pathlib import Path
from sqlalchemy import create_engine
from classes.consulta import Consulta
from consultas import queries
from datetime import datetime
from time import sleep

# Dados para acesso ao banco de dados para a EcoSystem

db_user = '_consulta'
db_pass = 'rzxtkwzj'
db_host = '192.168.70.15'
db_port = 3307
db_name = 'wingraph50'


db_url = f'mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_url)

# Consultas SQL

query_pos_calculo = queries.sql_pos_calculo
query_nome_operadores = queries.sql_nome_operadores


# Caminhos onde cada um dos arquivos retornados pelas consultas serão salvos

caminho_destino_pos_calc = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados PC\Pos_Calculo.xls')
caminho_destino_nome_ops = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados Ops\Operadores.xls')


# Instanciando objetos da classe Consulta

salvar_pos_calculo = Consulta(engine, query_pos_calculo, caminho_destino_pos_calc)
salvar_nome_ops = Consulta(engine, query_nome_operadores, caminho_destino_nome_ops)


try:
    salvar_pos_calculo.salvar_arquivo()
    salvar_nome_ops.salvar_arquivo()
    print(f'Pós Cálculo atualizado até {datetime.now().strftime('%H:%M:%S do dia %d/%m/%Y')}')

except: 
    print('Falha ao atualizar os dados')

finally:
    pass

sleep(10)