# a mesma coisa que eu fiz no .ipynb eu vou fazer aqui no pycharm(pd.py)
import pandas as pd
df = pd.read_csv(r"C:\Users\user\Desktop\grafico\Athlete\athlete_events.csv") 
print(df.head())
# uma boa diferença que você pode perceber no pycharm(gratis) para o jupyter é o uso de
# print() e nao no display por ter que colocar o df.head() dentro do print() então tome cuidado
#entao pra gráfico jupyter é um pouco melhor

#df.head() pode mostrar a quantidade de linhas que você quiser
print(df.head(0))  # ate linha zero
# como você pode ver o titulo esta em ingles, mas tem como mudar isso
#  NOC = Sigla( National Olympic Committee) traduzido = Comitês Olímpicos Nacionais (CON)

dif = df.rename(
    columns={'Name': 'Nome', 'Sex': "Sexo", "Age": 'Idade', 'Height': "Peso", "Weight": 'Altura', "Team": 'Time',
             'NOC': "CON", "Games": 'Jogos', "Year": 'Ano', 'Season': "Temporada", "City": 'Cidade', 'Sport': "Esporte",
             'Event': "Evento", "Medal": 'Medalha'})
print(dif.head())

# e também se você quiser te como pegar uma coluna especifica
altura = df["Weight"].head(10)
print(altura)
