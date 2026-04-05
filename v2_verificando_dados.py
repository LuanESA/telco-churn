from v1_dados import dados_arquivos
import pandas as pd

# Verificando se possui algum arquivo duplicado
df = dados_arquivos()
print("Linhas duplicadas:", df.duplicated().sum())
print("IDs duplicados:", df.duplicated(subset='customerID').sum())

# Verificando se possui algum espaço em branco
print(df.isnull().sum())
print((df == " ").sum())



# verificando os tipos de dados das colunas
df.head()
df.info()

# Verificando as colunas, todas as colunas demonstram ser de interesse para nossa análise.
# Iremos manter a coluna de ID apenas para organização e evitar duplicatas, tanto para rastreamento caso necessário.
# Analisando, verificamos que a coluna Total Charges está constando como objeto, que deveria ser um float.
# Portanto iremos converter a coluna.
# Aqui utilizando o erros='coerce' porque na coluna possuia alguns valores em branco, assim convertendo para NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.info()



# exportando o arquivo

df.to_csv('raw/dados_tratados.csv', index=False)