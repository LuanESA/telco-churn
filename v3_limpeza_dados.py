import pandas as pd
from config import COLUNAS_SERVICOS

def dados_tratados(df):
    df = df.copy()

    # Converter TotalCharges de object para float
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')


    # Remover linhas com TotalCharges nulo
    #    (são clientes com tenure=0, provavelmente cadastros novos
    #    que não geraram cobrança ainda — representam <0,2% da base)
    df.dropna(subset=['TotalCharges'], inplace=True)


    # Converter Churn para binário (0 = Não, 1 = Sim)
    df['Churn'] = df['Churn'].nap({'Yes': 1, 'No': 0})


    # Criar coluna de faixa de preço mensal
    df['faixa_preco'] = pd.cut(
        df['MonthlyCharges'],
        bins=5,
        labels=['Muito Baixo', 'Baixo', 'Médio', 'Alto', 'Muito Alto']
    )


    # Criar coluna de grupo de tempo de empresa (tenure)
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, 72],
        labels=['0-12 meses', '12-24 meses', '24-48 meses', '48-60 meses', '60-72 meses']
    )


    # Criar coluna com contagem de serviços adicionais
    df['n_servicos'] = df[COLUNAS_SERVICOS].apply(
        lambda row: (row == 'Yes').sum(), axis=1
    )

    return df

