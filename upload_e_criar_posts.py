import os
import requests
from requests.auth import HTTPBasicAuth
from config import wordpress_url, username, password

# Função para fazer o upload de imagens


def upload_imagem(caminho_imagem):
    nome_arquivo = os.path.basename(caminho_imagem)  # Extrair o nome da imagem
    headers = {
        "Content-Disposition": f"attachment; filename={nome_arquivo}"
    }
    try:
        with open(caminho_imagem, "rb") as arquivo:
            response = requests.post(
                f"{wordpress_url}/wp/v2/media",
                files={"file": arquivo},
                headers=headers,
                auth=HTTPBasicAuth(username, password)
            )
            if response.status_code == 201:
                json_response = response.json()
                if isinstance(json_response, list):
                    # Pega o primeiro item se for uma lista
                    json_response = json_response[0]
                print(f"Imagem '{nome_arquivo}' indexada com sucesso!")
                return json_response  # Retorna os detalhes da imagem indexada
            else:
                print(
                    f"Erro ao indexar a imagem '{nome_arquivo}': {response.status_code}")
                print(response.text)
                return None
    except Exception as e:
        print(f"Erro ao tentar fazer upload da imagem '{nome_arquivo}': {e}")
        return None

# Função para criar posts e definir imagem destacada


def criar_post_com_imagem_destacada(titulo, conteudo, pagina_especifica_id, id_imagem_destacada):
    try:
        dados_post = {
            "title": titulo,
            "content": conteudo,
            "status": "publish",  # Publicar imediatamente
            "parent": pagina_especifica_id,  # Associar o post à página específica
            "featured_media": id_imagem_destacada,  # Definir a imagem destacada
        }
        response = requests.post(
            f"{wordpress_url}/wp/v2/posts",
            json=dados_post,
            auth=HTTPBasicAuth(username, password)
        )
        if response.status_code == 201:
            print(f"Post '{titulo}' criado com sucesso com imagem destacada!")
            return response.json()
        else:
            print(f"Erro ao criar o post '{titulo}': {response.status_code}")
            print(response.text)
            return None
    except requests.RequestException as e:
        print(f"Erro ao tentar criar o post '{titulo}': {e}")
        return None

# Função principal para indexar imagens e criar posts


def processar_imagens(diretorio_base, pagina_especifica_id):
    if not os.path.isdir(diretorio_base):
        print(f"Diretório não encontrado: {diretorio_base}")
        return

    for raiz, _, arquivos in os.walk(diretorio_base):
        for arquivo in arquivos:
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                caminho_imagem = os.path.join(raiz, arquivo)
                detalhes_imagem = upload_imagem(caminho_imagem)

                if detalhes_imagem and isinstance(detalhes_imagem, dict):
                    url_imagem = detalhes_imagem.get("source_url", "")
                    id_imagem_destacada = detalhes_imagem.get("id", "")

                    if not url_imagem or not id_imagem_destacada:
                        print(
                            f"Erro: Detalhes da imagem '{arquivo}' não encontrados corretamente.")
                        continue

                    titulo_imagem = os.path.splitext(arquivo)[0]
                    conteudo_post = f"<img src='{url_imagem}' alt='{titulo_imagem}' />"

                    criar_post_com_imagem_destacada(
                        titulo_imagem, conteudo_post, pagina_especifica_id, id_imagem_destacada
                    )


# Configurações
diretorio_base = r"C:\Users\teste\OneDrive\Imagens\Campanha Cromatografos 2"
pagina_especifica_id = 1069  # Substitua pelo ID da página específica

# Processar as imagens e criar os posts com imagens destacadas
processar_imagens(diretorio_base, pagina_especifica_id)
