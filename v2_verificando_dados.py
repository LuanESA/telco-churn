from v1_dados import dados_arquivos
import pandas as pd

# ============================================================
# v2_verificando_dados.py
# Responsabilidade: APENAS verificar a qualidade dos dados brutos.
# Nenhuma transformação é feita aqui.
# ============================================================

df = dados_arquivos()

print("=" * 50)
print("VERIFICAÇÃO DE DUPLICATAS")
print("=" * 50)
print("Linhas duplicadas:", df.duplicated().sum())
print("IDs duplicados:", df.duplicated(subset='customerID').sum())

print("\n" + "=" * 50)
print("VALORES NULOS POR COLUNA")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("VALORES EM BRANCO (espaço) POR COLUNA")
print("=" * 50)
print((df == " ").sum())

print("\n" + "=" * 50)
print("TIPOS DE DADOS")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("PRIMEIRAS LINHAS")
print("=" * 50)
print(df.head())

# Observação: a coluna TotalCharges está como object mas deveria ser float.
# Isso ocorre porque há valores em branco que impedem a conversão automática.
# A limpeza e conversão é feita no v3_limpeza_dados.py.