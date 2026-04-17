import pandas as pd

def dados_tratados(df):
    df = df.copy()

    # convertendo total charges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # tratando os NaN gerados
    df.dropna(subset=['TotalCharges'], inplace=True)

    # convertendo churn para binário
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # convertendo SeniorCitizen para binário
    df['SeniorCitizen'] = df['SeniorCitizen'].map({'Yes': 1, 'No': 0})

    return df


# carregar dados
df = pd.read_csv('raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# aplicar função
df = dados_tratados(df)

# exportar
df.to_csv('raw/dados_tratados.csv', index=False)

