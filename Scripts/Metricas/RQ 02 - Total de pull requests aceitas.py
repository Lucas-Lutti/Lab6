import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Supondo que a função converter_dias_para_texto possa ser adaptada para outro contexto se necessário
def converter_numeros_para_texto(numero):
    # Uma função hipotética que poderia converter números em uma representação textual relevante
    # Aqui, simplesmente retornaremos o número em formato string para exemplo
    return str(numero)

caminho_arquivo = '/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts/repositories.csv'
df = pd.read_csv(caminho_arquivo)

bins = [0, 10, 50, 100, 500, 1000, 5000, 10000, df['mergedPRs'].max()]
df['prs_faixa'] = pd.cut(df['mergedPRs'], bins=bins, right=False)
faixa_contagem = df['prs_faixa'].value_counts(sort=False)

# Adicionando análise descritiva para 'mergedPRs'
analise_descritiva_prs = df['mergedPRs'].describe()

# Dicionário de explicações poderia ser adaptado se fosse aplicável para PRs
explicacoes_prs = {
    "count": "Número de entradas não nulas.",
    "mean": "Média aritmética dos dados.",
    "std": "Desvio padrão, indicando a dispersão dos dados.",
    "min": "Menor valor encontrado.",
    "25%": "Valor abaixo do qual estão 25% dos dados (primeiro quartil).",
    "50%": "Mediana, o valor do meio dos dados.",
    "75%": "Valor abaixo do qual estão 75% dos dados (terceiro quartil).",
    "max": "Maior valor encontrado."
}

print("Análise descritiva do número de PRs aceitas nos repositórios:")
for stat in analise_descritiva_prs.index:
    valor = analise_descritiva_prs[stat]
    if stat in ['mean', 'min', '25%', '50%', '75%', 'max']:
        print(f"{stat} ({explicacoes_prs[stat]}): {converter_numeros_para_texto(valor)}")
    else:
        print(f"{stat} ({explicacoes_prs[stat]}): {valor}")

# Plotando o histograma para faixas de PRs aceitas
faixa_contagem.plot(kind='bar', figsize=(10, 6), color='skyblue', edgecolor='black')
plt.title('Quantidade de Repositórios por Faixa de Pull Requests Aceitas')
plt.xlabel('Faixa de Pull Requests Aceitas')
plt.ylabel('Quantidade de Repositórios')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.show()
