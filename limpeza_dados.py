import pandas as pd

def dados_tratados(df):
    df = df.copy()

    # converter coluna TotalCharges para número
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df
