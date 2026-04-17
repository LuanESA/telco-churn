import pandas as pd
from config import RAW_DATA_PATH
 
 
def dados_arquivos():
    df = pd.read_csv(RAW_DATA_PATH)
    return df