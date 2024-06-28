# %%
import pandas as pd
# %%
pd.__version__
# %%
# Series: dados em colunas (1 dimnesão)
# Dataframes: dados em 2 dimensões (linhas e colunas)

carros = pd.Series(["Toyota", "Honda", "BMW"])
cores = pd.Series(["Azul", "Branco", "Vermelho"])
# %%
print(carros)
print(type(carros))
# %%
# criando DF e associando com Séries anteriores
df = pd.DataFrame({"Fabricante": carros,
                   "Cores": cores})
# %%
print(df)
print(type(df))


# %%
# cada coluna do Dataframe é uma Serie
print(df['Fabricante'])
print(type(df['Fabricante']))
# %%
path_data = 'ml-book-exemplos-main/data/'
df = pd.read_csv(path_data+'venda-de-carros.csv')
df
# %%
#coluna preço tem formato de object -> estrutura monetária
df.dtypes
# %%
# visão estatística de todas as colunas numéricas
df.describe()
# %%
# mostra quantas linhas existem, se há valores 
# ausentes e os tipos de dados de cada coluna:
df.info()
# %%
# mean e sum
valores = pd.Series([3000, 3500, 11250])
print('mean: ',valores.mean())
print('sum: ',valores.sum())
# %%
# aplicar funções estatística em um DF inteiro, não faz sentido
# aplicar diretamente nas colunas
print('colunas disponíveis', df.columns)
print('media Quilometragem: ', df['Quilometragem'].mean())
# %%
# default = 5
df.head(2)
# %%
# default = 5
df.tail(2)
# %%
# loc e iloc
# loc: traz dado com índice x (índice da serie/df)
# iloc: traz dado na posição y (começando em 0)
animais = pd.Series(["gato", "ave", "cachorro", "cobra", "leão", "cavalo"], 
                   index=[0, 3, 8, 9, 6, 3])
animais
# serie com indices trocados (não-padrão)
# %%
# traz elementos com índice 3
animais.loc[3]
# %%
# traz elemento na posição 3 da serie (4º elemento)
animais.iloc[3]

# %%
df
# %%
df.loc[3]
# %%
df.iloc[3]
# %%
# Ambos .loc[] e .iloc[] retornaram o mesmo valor 
# pois as informações no DataFrame exibidas estão 
# em ordem tanto na posição quanto no índice.
# %%
# slicing
print(animais)
print("\ntrazer todos os elementos do início até posição 3 (não inclusa)")
print(animais.iloc[:3])
# %%
# filtros

filtro = df['Quilometragem'] > 100000
df[filtro]
# %%
df[df["Fabricante"]=='Honda']
# %%
# groupby
print('agrupar os dados por fabricante e calcular a média das colunas numéricas')

df.groupby(["Fabricante"]).mean(numeric_only=True)

# %%
#ajustar coluna de preço -> remover R$ e vírgula (,)
df['Preco'] = df["Preco"].str.replace('[/R$/,]', '', regex=True)
df
# %%
df.dtypes
# %%
df['Preco'] = pd.to_numeric(df['Preco'])
df.dtypes


# %%
df2 = pd.read_csv(path_data+"venda-de-carros-dados-ausentes.csv")
df2
# %%
df2['Quilometragem'].fillna(df2['Quilometragem'].mean(), inplace=True)
df2
# %%
df2.dropna(inplace=True)
df2
# %%
qtde_assentos = pd.Series([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
df['Assentos'] = qtde_assentos
df
# %%
motor_lista = [1.3, 2.0, 3.0, 4.2, 1.6, 1, 2.0, 2.3, 2.0, 3.0]
df['Motor'] = motor_lista
df
# %%
df["Preco por KM"] = df["Preco"] / df["Quilometragem"]
df
# %%
df = df.drop("Preco por KM", axis=1)
df
# %%
# embaralhar a ordem do seu DataFrame para poder dividi-lo 
# em conjuntos de treinamento, teste e validação
df_sample = df.sample(frac=1)
df_sample

# %%
df_sample.reset_index(inplace=True)
df_sample
# %%
