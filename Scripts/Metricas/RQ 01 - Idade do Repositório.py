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

df = pd.read_csv('repositories.csv')

df['createdAt'] = pd.to_datetime(df['createdAt']).dt.tz_localize(None)

now_naive = datetime.now()

df['repo_age_days'] = (now_naive - df['createdAt']).dt.days

analise_descritiva = df['repo_age_days'].describe()

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

print("Análise descritiva das idades dos repositórios:")
for stat in analise_descritiva.index:
    valor = analise_descritiva[stat]
    if stat in ['mean', 'min', '25%', '50%', '75%', 'max']:
        print(f"{stat} ({explicacoes[stat]}): {converter_dias_para_texto(valor)}")
    else:
        print(f"{stat} ({explicacoes[stat]}): {valor}")


# Calcula a idade dos repositórios em anos para o histograma
df['repo_age_years'] = df['repo_age_days'] / 365.25

# Gera o histograma
plt.figure(figsize=(10, 6))
plt.hist(df['repo_age_years'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição da Idade dos Repositórios')
plt.xlabel('Idade (Anos)')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)

y_max = plt.ylim()[1]  
for stat in ['mean', '50%', 'min', 'max']:
    valor_dias = analise_descritiva[stat]
    texto = f"{stat}: {converter_dias_para_texto(valor_dias)}"
    plt.text(df['repo_age_years'].max(), y_max * (0.92 if stat == 'mean' else (0.84 if stat == '50%' else (0.76 if stat == 'min' else 0.68))), texto, ha='right')

plt.show()