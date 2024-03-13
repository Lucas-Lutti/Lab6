import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

caminho_arquivo = '/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts/repositories.csv'
df = pd.read_csv(caminho_arquivo)

bins = [0, 10, 50, 100, 500, 1000, 5000, 10000, df['mergedPRs'].max()]

df['prs_faixa'] = pd.cut(df['mergedPRs'], bins=bins, right=False)

faixa_contagem = df['prs_faixa'].value_counts(sort=False)

faixa_contagem.plot(kind='bar', figsize=(10, 6), color='skyblue', edgecolor='black')
plt.title('Quantidade de Repositórios por Faixa de Pull Requests Aceitas')
plt.xlabel('Faixa de Pull Requests Aceitas')
plt.ylabel('Quantidade de Repositórios')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)

plt.show()
