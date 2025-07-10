import requests
from requests.auth import HTTPBasicAuth
from config import wordpress_url, username, password

# Configuração de autenticação
auth = HTTPBasicAuth(username, password)

def test_api_connection(wp_url, auth):
    try:
        response = requests.get(f"{wp_url}/wp/v2/pages", auth=auth)
        response.raise_for_status()  # Lança um erro se a resposta for ruim (4xx ou 5xx)

        pages = response.json()
        print("Conexão com a API bem-sucedida! 🎉\n")
        print("Páginas encontradas:")

        for page in pages:
            print(f"- ID: {page['id']} | Título: {page['title']['rendered']}")

    except requests.RequestException as e:
        print(f"Erro ao conectar à API: {e}")

# Executar teste
test_api_connection(wordpress_url, auth)
