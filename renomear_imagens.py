import os
import shutil

# Caminho da pasta onde estão suas imagens originais
pasta_origem = r"C:\Users\teste\Downloads\CAMPANHA HOSPITAL MAC GOIANIA GOIAS"
# Caminho onde serão salvas as cópias renomeadas
pasta_destino = r"C:\Users\teste\Downloads\CAMPANHA HOSPITAL MAC GOIANIA GOIAS\CAMPANHA"

# Garante que a pasta de destino existe
os.makedirs(pasta_destino, exist_ok=True)

# Lista de nomes base das imagens (sem extensão)
nomes = [
    "IMAC", "IPAD", "MACBOOK", "MACBOOK-AIR", "MACBOOK-APPLE",
    "MAC-PRO", "PCB-IMAC", "PCB-MACBOOK", "PLACA-MÃE-", "PLACA-MÃE-IMAC", "PLACA-MÃE-MACBOOK",
    "TELA-IMAC", "TELA-IPAD", "TELA-MACBOOK", "TELA-MACBOOK-AIR"
]

# Variações de nomes a serem aplicadas
variacoes = [
    "ASSISTENCIA-TECNICA-APPLE-{marca}-GOIANIA",
    "ASSISTENCIA-TECNICA-APPLE-{marca}-GOIANIA",
    "ASSISTENCIA-TECNICA-AUTORIZADA-APPLE-{marca}-GOIANIA-GO",
    "ASSISTENCIA-APPLE-{marca}-GOIANIA-GOIAS",
    "ASSISTENCIA-APPLE-APPLE-{marca}-GOIANIA",
    "CONSERTO-APPLE-{marca}-GOIANIA",
    "REPARO-APPLE-{marca}-GOIANIA",
    "MANUTENCAO-APPLE-{marca}-GOIANIA",
    "REPARO-APPLE-{marca}-GOIANIA",
    "CONSERTO-APPLE-{marca}-GOIANIA-GO",
    "REPARO-E-MANUTENCAO-APPLE-{marca}-GOIANIA",
    "MANUTENCAO-E-CONSERTO-APPLE-{marca}-GOIANIA",
    "MANUTENCAO-DE-APPLE-{marca}-GOIANIA-GO",
    "CONSERTO-DE-APPLE-{marca}-GOIANIA-GOIAS",
    "REPARO-DE-APPLE-{marca}-GOIANIA-GO",
    "SERVICO-DE-MANUTENCAO-APPLE-{marca}-GOIANIA",
    "ASSISTENCIA-TECNICA-PARA-APPLE-{marca}-EM-GOIANIA",
    "ASSISTENCIA-TECNICA-{marca}-APPLE-GOIANIA",
    "ASSISTENCIA-{marca}-APPLE-GOIANIA-GO",
    "SUPORTE-TÉCNICO-APPLE-{marca}-GOIANIA",
    "SERVICOS-DE-REPARO-APPLE-{marca}-GO",
    "AUTORIZADA-APPLE-{marca}-GOIANIA",
    "ASSISTENCIA-APPLE-MARCA-{marca}-GOIANIA-GO",
    "APPLE-{marca}-REPARO-E-MANUTENCAO-GOIANIA-GO",
    "ASSISTENCIA-TECNICA-APPLE-{marca}-GOIANIA-GO",
    "ASSISTENCIA-{marca}-GOIANIA-APPLE",
    "APPLE-{marca}-CONSERTO-GOIANIA-GOIAS",
    "APPLE-{marca}-REPARO-GOIANIA-GO",
    "MANUTENCAO-{marca}-APPLE-GOIANIA",
    "ASSISTENCIA-{marca}-AUTORIZADA-GOIANIA-APPLE"
]


# Extensão das imagens
extensao = ".png"

# Loop para cada imagem original
for nome in nomes:
    nome_arquivo_origem = os.path.join(pasta_origem, nome + extensao)

    if not os.path.exists(nome_arquivo_origem):
        print(f"❌ Imagem {nome_arquivo_origem} não encontrada.")
        continue

    for i, variacao in enumerate(variacoes):
        novo_nome = variacao.replace("{marca}", nome) + extensao
        destino = os.path.join(pasta_destino, novo_nome)

        shutil.copy(nome_arquivo_origem, destino)
        print(f"✅ Copiado: {nome_arquivo_origem} ➝ {destino}")
