import requests
import json

headers = {
    "Authorization": "Bearer xxxx",  # Substitua pelo seu token real
    "Accept": "application/vnd.github.v3+json"
}

def generate_query(after_cursor=None):
    after_cursor_str = f', after: "{after_cursor}"' if after_cursor else ""
    return f"""
    {{
      search(query: "stars:>1", type: REPOSITORY, first: 10{after_cursor_str}) {{
        pageInfo {{
          endCursor
          hasNextPage
        }}
        edges {{
          node {{
            ... on Repository {{
              name
              createdAt
              updatedAt
              owner {{
                login
              }}
              primaryLanguage {{
                name
              }}
              pullRequests(states: MERGED) {{
                totalCount
              }}
              releases {{
                totalCount
              }}
              issues(states: CLOSED) {{
                totalCount
              }}
              totalIssues: issues {{
                totalCount
              }}
              stargazers {{
                totalCount
              }}
            }}
          }}
        }}
      }}
    }}
    """

def fetch_repositories():
    has_next_page = True
    after_cursor = None
    all_repositories = []  # Lista para armazenar os dados dos repositórios
    total_repos_collected = 0  # Contador para o número total de repositórios coletados

    while has_next_page and total_repos_collected < 100:
        query = generate_query(after_cursor)
        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            edges = response_data['data']['search']['edges']
            all_repositories.extend(edges)  # Adiciona os dados à lista
            total_repos_collected += len(edges)  # Atualiza o contador de repositórios

            # Preparar para a próxima página
            page_info = response_data['data']['search']['pageInfo']
            has_next_page = page_info['hasNextPage'] and total_repos_collected < 100
            after_cursor = page_info['endCursor']
        else:
            print(f"Falha na consulta: {response.status_code}")
            return  # Finaliza a função em caso de erro

    # Cortar a lista para ter exatamente 100 repositórios, caso tenha excedido
    all_repositories = all_repositories[:100]

    # Após coletar os dados, escrever em um arquivo JSON
    with open('consulta100rep.json', 'w') as file:
        json.dump(all_repositories, file, indent=4)
    print("Os dados dos repositórios foram salvos em 'consulta100rep.json'")

# Chamar a função para iniciar a busca paginada e salvar os resultados
fetch_repositories()
