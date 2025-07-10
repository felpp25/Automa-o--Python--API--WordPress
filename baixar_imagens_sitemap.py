import requests
from lxml import html
import os
from urllib.parse import urlparse

# URL do sitemap
SITEMAP_URL = "http://hospitaldomac.com.br/page-sitemap.xml"

# Pasta onde as imagens serão salvas
PASTA_DESTINO = "imagens_apple"

# Criar a pasta se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)


def baixar_sitemap(url):
    print(f"🔍 Baixando sitemap: {url}")
    resposta = requests.get(url)
    soup = html.fromstring(resposta.content)
    urls = soup.xpath('//url/loc/text()')
    print(f"📄 Total de posts encontrados: {len(urls)}")
    return urls


def extrair_imagem(post_url):
    try:
        print(f"➡️ Acessando: {post_url}")
        resposta = requests.get(post_url, timeout=10)
        arvore = html.fromstring(resposta.content)

        # XPath fornecido
        imagem = arvore.xpath('//*[@id="content"]/div/div/div/section/div/div/div/div/div/div[2]/div/div/img')

        if imagem and 'src' in imagem[0].attrib:
            return imagem[0].attrib['src']
    except Exception as e:
        print(f"⚠️ Erro ao processar {post_url}: {e}")
    return None


def baixar_imagem(url_imagem):
    nome_arquivo = os.path.basename(urlparse(url_imagem).path)
    caminho = os.path.join(PASTA_DESTINO, nome_arquivo)
    try:
        print(f"⬇️ Baixando imagem: {url_imagem}")
        img_data = requests.get(url_imagem).content
        with open(caminho, 'wb') as f:
            f.write(img_data)
        print(f"✅ Salvo como: {caminho}")
    except Exception as e:
        print(f"❌ Erro ao baixar {url_imagem}: {e}")


def main():
    posts = baixar_sitemap(SITEMAP_URL)
    for post_url in posts:
        url_imagem = extrair_imagem(post_url)
        if url_imagem:
            baixar_imagem(url_imagem)
        else:
            print("🚫 Nenhuma imagem encontrada.")


if __name__ == "__main__":
    main()
