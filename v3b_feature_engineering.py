# criando algumas colunas auxiliares
import pandas as pd
from v3_limpeza_dados import df

df['faixa_preco'] = pd.cut(df['MonthlyCharges'], bins=5);

