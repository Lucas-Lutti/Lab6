import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def converter_dias_para_texto(dias):
    """Converte um número de dias em uma string formatada em anos, meses e dias."""
    anos = int(dias // 365.25)
    dias_restantes = dias % 365.25
    meses = int(dias_restantes // 30.4375)
    dias = int(dias_restantes % 30.4375)
    return f"{anos} anos, {meses} meses e {dias} dias"

novo_diretorio = '/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts'
os.chdir(novo_diretorio)

# Carrega os dados
df = pd.read_csv('repositories.csv')

# Usa 'updatedAt' em vez de 'lastUpdate'
df['updatedAt'] = pd.to_datetime(df['updatedAt']).dt.tz_localize(None)

now_naive = datetime.now()

# Calcula o tempo desde a última atualização em dias
df['days_since_last_update'] = (now_naive - df['updatedAt']).dt.days

analise_descritiva = df['days_since_last_update'].describe()

explicacoes = {
    "count": "Número de entradas não nulas.",
    "mean": "Média aritmética dos dados.",
    "std": "Desvio padrão, indicando a dispersão dos dados.",
    "min": "Menor valor encontrado.",
    "25%": "Abaixo deste valor estão 25% dos dados (primeiro quartil).",
    "50%": "Mediana, o valor do meio dos dados.",
    "75%": "Abaixo deste valor estão 75% dos dados (terceiro quartil).",
    "max": "Maior valor encontrado."
}

print("Análise descritiva do tempo desde a última atualização dos repositórios:")
for stat in analise_descritiva.index:
    valor = analise_descritiva[stat]
    if stat in ['mean', 'min', '25%', '50%', '75%', 'max']:
        print(f"{stat} ({explicacoes[stat]}): {converter_dias_para_texto(valor)}")
    else:
        print(f"{stat} ({explicacoes[stat]}): {valor}")

# Gera o histograma mostrando o tempo desde a última atualização em dias
plt.figure(figsize=(10, 6))
plt.hist(df['days_since_last_update'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição do Tempo Desde a Última Atualização dos Repositórios (Dias)')
plt.xlabel('Tempo Desde Última Atualização (Dias)')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)

plt.show()
