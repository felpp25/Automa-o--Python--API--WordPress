import requests
import time
from requests.auth import HTTPBasicAuth
from config import wordpress_url, username, password

def obter_posts_para_atualizar():
    """Obtém apenas os posts que precisam ser atualizados, evitando requisições desnecessárias."""
    posts_para_atualizar = []
    page = 1

    while True:
        resposta = requests.get(
            f"{wordpress_url}/wp/v2/posts",
            params={"per_page": 100, "page": page},
            auth=HTTPBasicAuth(username, password),
            timeout=30
        )

        if resposta.status_code == 200:
            dados = resposta.json()
            if not dados:
                break  # Sai do loop se não houver mais posts

            # Filtra os posts que precisam ser atualizados
            for post in dados:
                if post.get("comment_status") == "open" or post.get("ping_status") == "open":
                    posts_para_atualizar.append(post["id"])
            
            page += 1  # Vai para a próxima página
        else:
            print(f"Erro ao obter posts na página {page}: {resposta.status_code} - {resposta.text}")
            break

    return posts_para_atualizar

def atualizar_post(post_id):
    """Atualiza um post desativando comentários e pings."""
    dados_atualizacao = {
        "comment_status": "closed",  # Desativa comentários
        "ping_status": "closed"      # Desativa pings
    }

    resposta = requests.post(
        f"{wordpress_url}/wp/v2/posts/{post_id}",
        json=dados_atualizacao,
        auth=HTTPBasicAuth(username, password),
        timeout=30
    )

    if resposta.status_code == 200:
        print(f"✅ Post {post_id} atualizado com sucesso!")
    else:
        print(f"⚠️ Erro ao atualizar post {post_id}: {resposta.status_code} - {resposta.text}")

def atualizar_posts_filtrados():
    """Busca e atualiza apenas os posts que realmente precisam de atualização."""
    posts_para_atualizar = obter_posts_para_atualizar()

    if not posts_para_atualizar:
        print("Todos os posts já estão configurados corretamente. Nenhuma atualização necessária.")
        return

    print(f"Total de posts a serem atualizados: {len(posts_para_atualizar)}")

    for post_id in posts_para_atualizar:
        atualizar_post(post_id)
        time.sleep(1)  # Pequeno delay para evitar bloqueios da API

# Executa a atualização
atualizar_posts_filtrados()
