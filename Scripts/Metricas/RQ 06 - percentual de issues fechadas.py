import os
import pandas as pd
import matplotlib.pyplot as plt

novo_diretorio = '/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts'
os.chdir(novo_diretorio)

df = pd.read_csv('repositories.csv')

print("Colunas no DataFrame:", df.columns.tolist())

df['closed_issues_ratio'] = df['closedIssues'] / (df['totalIssues'] + 0.0001)

df_filtered = df[df['totalIssues'] > 0]

df_sorted = df_filtered.sort_values(by='closed_issues_ratio', ascending=False)

print("Repositórios com os maiores percentuais de issues fechadas:")
print(df_sorted[['name', 'closed_issues_ratio']].head(10))

plt.figure(figsize=(10, 6))
plt.hist(df_filtered['closed_issues_ratio'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição do Percentual de Issues Fechadas')
plt.xlabel('Razão de Issues Fechadas')
plt.ylabel('Quantidade de Repositórios')
plt.grid(axis='y', alpha=0.75)
plt.show()
