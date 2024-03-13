import os
import pandas as pd
import matplotlib.pyplot as plt

novo_diretorio = '/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts'
os.chdir(novo_diretorio)

df = pd.read_csv('repositories.csv')


print("Colunas no DataFrame:", df.columns.tolist())


linguagens_primarias_contagem = df['primaryLanguage'].value_counts()

print("Linguagens primárias mais populares nos repositórios:")
print(linguagens_primarias_contagem)


plt.figure(figsize=(10, 6))
linguagens_primarias_contagem.plot(kind='bar')
plt.title('Popularidade das Linguagens Primárias nos Repositórios')
plt.xlabel('Linguagem Primária')
plt.ylabel('Quantidade de Repositórios')
plt.xticks(rotation=45)
plt.show()
