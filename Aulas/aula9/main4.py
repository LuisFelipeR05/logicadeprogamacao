import pandas as pd

df  = pd.read_csv("vendas_padaria.csv")


print(df.head)


print(df.tail())


print(df.info)


print(df['Preço_unitario'])