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
query_faturamento = queries.sql_faturamento
query_pedidos = queries.sql_pedidos
query_produtividade = queries.sql_produtividade

# Caminhos onde cada um dos arquivos retornados pelas consultas serão salvos

caminho_destino_pos_calc = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados\Pos_Calculo.xls')
caminho_destino_nome_ops = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados\Operadores.xls')
caminho_destino_pedidos = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados\Pedidos de Venda.xls')
caminho_destino_faturamento = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados\Notas Faturadas.xls')
caminho_destino_produtividade = Path(r'I:\ECOQUALITY\11. MONITORAMENTO DA PRODUÇÃO\Pós Cálculo\Dados\Produtividade por Op.xls')
# Instanciando objetos da classe Consulta

salvar_pos_calculo = Consulta(engine, query_pos_calculo, caminho_destino_pos_calc)
salvar_nome_ops = Consulta(engine, query_nome_operadores, caminho_destino_nome_ops)
salvar_pedidos = Consulta(engine, query_pedidos, caminho_destino_pedidos)
salvar_faturamento = Consulta(engine, query_faturamento, caminho_destino_faturamento)
salvar_produtividade = Consulta(engine, query_produtividade, caminho_destino_produtividade)


try:
    salvar_pos_calculo.salvar_arquivo()
    salvar_nome_ops.salvar_arquivo()
    salvar_pedidos.salvar_arquivo()
    salvar_faturamento.salvar_arquivo()
    salvar_produtividade.salvar_arquivo()
    print(f'Dados atualizado até {datetime.now().strftime("%H:%M:%S do dia %d/%m/%Y")}')


except: 
    print('Falha ao atualizar os dados')

finally:
    pass

sleep(10)