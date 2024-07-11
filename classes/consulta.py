import pandas as pd

class Consulta:
    def __init__(self, engine, query, caminho_destino) -> None:
        self._engine = engine
        self._caminho_destino = caminho_destino
        self._query = query

    def salvar_arquivo(self):
        df = pd.read_sql_query(self._query, self._engine).drop_duplicates()
        df.to_excel(self._caminho_destino, index=False)

    def testar(self):
        print('teste')


        




            
            

    


        
    