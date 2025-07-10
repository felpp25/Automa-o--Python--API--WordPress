import requests
from config import wordpress_url, username, password

# 🔗 Endpoint da API REST
api_url = f"{wordpress_url}/wp/v2/posts"

# 🔐 Autenticação
auth = (username, password)

# 🚀 Função para obter todos os posts (paginando)
def get_all_posts():
    posts = []
    page = 1
    while True:
        print(f"🔎 Buscando página {page}...")
        response = requests.get(api_url, auth=auth, params={'per_page': 100, 'page': page})
        
        if response.status_code != 200:
            print(f"❌ Erro ao buscar posts: {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        if not data:
            break
        
        posts.extend(data)
        page += 1
    
    print(f"✅ Total de {len(posts)} posts encontrados.")
    return posts


# ✍️ Função para atualizar título e slug
def update_post_title_slug(post):
    post_id = post['id']
    title = post['title']['rendered']
    slug = post['slug']
    
    # Verifica se tem "_" no título ou no slug
    if "_" not in title and "_" not in slug:
        print(f"➡️ Post ID {post_id} não precisa de alteração.")
        return
    
    # Cria os novos títulos e slugs
    new_title = title.replace("_", "-")
    new_slug = slug.replace("_", "-")
    
    print(f"🛠️ Atualizando Post ID {post_id}:")
    print(f"   🔤 Título: '{title}' ➝ '{new_title}'")
    print(f"   🔗 Slug: '{slug}' ➝ '{new_slug}'")
    
    # Dados para atualização
    data = {
        "title": new_title,
        "slug": new_slug
    }
    
    # Faz a requisição de atualização
    response = requests.post(f"{api_url}/{post_id}", auth=auth, json=data)
    
    if response.status_code == 200:
        print(f"✔️ Post ID {post_id} atualizado com sucesso!")
    else:
        print(f"❌ Erro ao atualizar Post ID {post_id}: {response.status_code}")
        print(response.text)


# 🔥 Executando tudo
if __name__ == "__main__":
    posts = get_all_posts()
    print("\n🚀 Iniciando atualizações...\n")
    for post in posts:
        update_post_title_slug(post)

    print("\n🎉 Atualização concluída!")
