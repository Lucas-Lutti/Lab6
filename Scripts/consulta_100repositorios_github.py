import requests
import json  # Importe o módulo json

# Substitua 'YOUR_ACCESS_TOKEN' pelo seu token de acesso pessoal do GitHub
headers = {"Authorization": "Bearer xxxx"}

# Consulta GraphQL
query = """
{
  search(query: "stars:>1", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          name
          createdAt
          updatedAt
          owner {
            login
          }
          primaryLanguage {
            name
          }
          pullRequests(states: MERGED) {
            totalCount
          }
          releases {
            totalCount
          }
          issues(states: CLOSED) {
            totalCount
          }
          totalIssues: issues {
            totalCount
          }
          stargazers {
            totalCount
          }
        }
      }
    }
  }
}
"""

# Enviar a consulta
response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

# Verificar se a consulta foi bem-sucedida
if response.status_code == 200:
    # Salvar a resposta em um arquivo JSON
    with open('resultado_consulta.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
    print("A resposta foi salva em 'resultado_consulta.json'")
else:
    print(f"Falha na consulta: {response.status_code}")
    # Imprime a resposta para ajudar no diagnóstico do problema
    print(response.text)
