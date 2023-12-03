
import pandas as pd

#Cria o DataFrame e lê o aquivo com os dados.
df = pd.read_csv('arquivo.csv')


#Exercício 0
#Imprime na tela as primeiras 5 linhas da tabela do aqruivo.
print(df.head(5))

#Exercício 01
#Imprime da tela o número de linhas e colunas.
print(df.shape)
