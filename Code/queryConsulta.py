import requests
import json
query = """{
  search(query: "stars:>0", type: REPOSITORY, first: 100) {
    repositoryCount
    edges {
      node {
        ... on Repository {
          name
          owner {
            login
          }
          stargazerCount
          url
          createdAt
          updatedAt
          primaryLanguage {
            name
          }
          pullRequests {
            totalCount
          }
         issues:issues {
            totalCount
          }
          closedIssues: issues (states: CLOSED) {
            totalCount
          }
        }
      }
    }
  }
}
"""
# GraphQL no Github
url = 'https://api.github.com/graphql'
token = 'gerar token'

headers = {
    'Authorization': f'bearer {token}',
    'Content-Type': 'application/json',
}

# Fazer a requisição POST com a consulta GraphQL
response = requests.post(url, headers=headers, json={'query': query})

# Só verifica se a requisição pra api foi bem sucedida
if response.status_code == 200:
    
    data = response.json()
    
    #Pega só o que importa (definido na query)
    repositories = data['data']['search']['edges']
    
    # Salvar os dados em um arquivo JSON
    with open('repositories.json', 'w') as f:
        json.dump(repositories, f, indent=4)
        
    print("Os dados foram salvos com sucesso no arquivo 'repositories.json'.")
else:
    print("Erro ao fazer a requisição à API GraphQL:", response.text)
