import os
import requests
from requests.auth import HTTPBasicAuth
from config import wordpress_url, username, password

# Configuração de autenticação
auth = HTTPBasicAuth(username, password)

# Caminho da imagem
image_path = r"C:\Users\teste\OneDrive\Área de Trabalho\Projeto ESAOTE\esaote_slide.webp"

# Função para fazer upload da imagem
def upload_image(image_path, wp_url, auth):
    try:
        with open(image_path, "rb") as img:
            filename = os.path.basename(image_path)
            headers = {
                "Content-Disposition": f"attachment; filename={filename}"
            }
            response = requests.post(
                f"{wp_url}/media", 
                headers=headers, 
                files={"file": img}, 
                auth=auth
            )
        
        response.raise_for_status()
        image_id = response.json().get("id")
        image_url = response.json().get("source_url")
        print(f"Imagem enviada com sucesso: {image_url}")
        return image_id, image_url
    except requests.RequestException as e:
        print(f"Erro ao enviar a imagem: {e}")
        return None, None

# Função para atualizar posts
def update_posts(image_id, image_url, wp_url, auth):
    try:
        response = requests.get(f"{wp_url}/posts", auth=auth)
        response.raise_for_status()
        posts = response.json()
        
        for post in posts:
            post_id = post.get("id")
            content = post.get("content", {}).get("rendered", "")
            new_content = f'<img src="{image_url}" alt="Imagem">\n' + content
            
            data = {
                "content": new_content,
                "featured_media": image_id
            }
            update_response = requests.post(
                f"{wp_url}/posts/{post_id}", json=data, auth=auth
            )
            update_response.raise_for_status()
            print(f"Post {post_id} atualizado com sucesso!")
    
    except requests.RequestException as e:
        print(f"Erro ao atualizar posts: {e}")

# Executar o script
image_id, image_url = upload_image(image_path, wordpress_url, auth)
if image_id:
    update_posts(image_id, image_url, wordpress_url, auth)
