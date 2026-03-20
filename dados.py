import pandas as pd

def dados_arquivos():
    df = pd.read_csv("archive/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df