import requests
import json
import csv
from datetime import datetime

headers = {
    "Authorization": "Bearer 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",  # Substitua SEU_TOKEN_AQUI pelo seu token real
}

def generate_query(after_cursor=None):
    after_cursor_str = f', after: "{after_cursor}"' if after_cursor else ""
    return f"""
    {{
      search(query: "stars:>1", type: REPOSITORY, first: 100{after_cursor_str}) {{
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
    all_repositories = []

    while has_next_page:
        query = generate_query(after_cursor)
        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            edges = response_data['data']['search']['edges']
            all_repositories.extend([{
                'name': edge['node']['name'],
                'owner': edge['node']['owner']['login'],
                'stars': edge['node']['stargazers']['totalCount'],
                'createdAt': edge['node']['createdAt'],
                'updatedAt': edge['node']['updatedAt'],
                'primaryLanguage': edge['node']['primaryLanguage']['name'] if edge['node']['primaryLanguage'] else '',
                'mergedPRs': edge['node']['pullRequests']['totalCount'],
                
                'closedIssues': edge['node']['issues']['totalCount'],
                'totalIssues': edge['node']['totalIssues']['totalCount']
            } for edge in edges])

            page_info = response_data['data']['search']['pageInfo']
            has_next_page = page_info['hasNextPage']
            after_cursor = page_info['endCursor']

            if len(all_repositories) >= 1000:
                break
        else:
            print(f"Falha na consulta: {response.status_code}")
            break

    return all_repositories[:1000]

def save_to_csv(repositories):
    fields = ['name', 'owner', 'stars', 'createdAt', 'updatedAt', 'primaryLanguage', 'mergedPRs', 'releases', 'closedIssues', 'totalIssues']
    with open('/Users/lucaspicinin/Desktop/Lab6/Laboratorio6.1/Lab6/Scripts/repositories.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for repo in repositories:
            writer.writerow(repo)

repositories = fetch_repositories()
save_to_csv(repositories)
print("Dados dos repositórios foram salvos com sucesso em repositories.csv.")
