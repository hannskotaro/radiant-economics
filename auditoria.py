# Importa a biblioteca Pandas
import pandas as pd

# Importa dados de um arquivo Excel de uma planilha específica e guarda em uma variável
dados = pd.read_excel('arquivo.xlsx', sheet_name='planilha_que_esta_as_colunas')

# Cria um Dicionário com um DataFrame referente a variavel
dfs = pd.DataFrame(dados)

# Calcula a diferença entre as colunas "coletado" e "declarado" e cria uma nova coluna com o "resultado"
dfs['resultado'] = dfs['coletado'] == dfs['declarado']

# Calcula a diferença percentual entre as colunas "coletado" e "declarado" e cria uma nova coluna com "percentual"
dfs['percentual'] = (dfs['coletado'] - dfs['declarado']) / dfs['declarado'] * 100

# Exibe o DataFrame resultante
print(dfs)
