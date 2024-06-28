# link exercício original: https://github.com/infoslack/ml-book-exemplos/blob/main/pandas_exercicios.ipynb

# %%
import pandas as pd
# %%
cores = pd.Series(['Vermelho', 'Verde', 'Preto'])
cores
# %%
fabricantes = pd.Series(['VW', 'Fiat', 'Ford'])
fabricantes
# %%
df = pd.DataFrame({'Cores':cores,'Fabricantes':fabricantes})
df
# %%
df_carros = pd.read_csv('ml-book-exemplos-main/data/venda-de-carros.csv')
df_carros
# %%
df_carros.dtypes
# %%
df_carros.describe()
# %%
df_carros.info()
# %%
df_carros.columns
# %%
df_carros.head()
# %%
df_carros.tail()
# %%
df_carros.loc[3]
# %%
df_carros.iloc[3]
# %%
df_carros['Quilometragem']
# %%
df_carros['Quilometragem'].mean(numeric_only=True)

# %%
df_carros[df_carros['Quilometragem'] > 100000]
# %%
df_carros.groupby(['Fabricante']).mean(['Quilometragem', 'Portas'])
# %%
df_carros['Preco']=df_carros['Preco'].str.replace('[/R$/,]','', regex=True)
df_carros
# %%
df_carros.info()
# %%
df_carros['Preco'] = pd.to_numeric(df_carros['Preco'])
df_carros.info()
# %%
df_carros.groupby(['Fabricante']).mean(numeric_only=True)
# %%
