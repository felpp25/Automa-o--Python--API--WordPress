import requests
from requests.auth import HTTPBasicAuth
from config import wordpress_url, username, password

# Função para criar uma página
def criar_pagina(titulo, conteudo):
    # Dados da página
    dados_pagina = {
        "title": titulo,
        "content": conteudo,
        "status": "publish"  # Publicar imediatamente
    }

    # Enviar a requisição para criar a página
    response = requests.post(f"{wordpress_url}/wp/v2/pages",
                             json=dados_pagina, auth=HTTPBasicAuth(username, password))

    if response.status_code == 201:  # Código 201 indica sucesso na criação
        print(f"Página '{titulo}' criada com sucesso!")
        return response.json()  # Retorna os detalhes da página criada
    else:
        print(f"Erro ao criar a página '{titulo}'. Status Code: {response.status_code}")
        print(response.text)
        return None

# Lista de páginas a serem criadas (sem a página "Home")
paginas = [
    {"titulo": "CONCERTO-CROMATOGRAFOS-AGILENTHP-10544A-CRISTAL-OSCILADOR-10-MHZ-COM-BASE-DE-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-19624-AGILENT-PCB-PLACA-DE-PINOS-335013-E312626611-E312666611", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-34456-AGILENT-PCB-PLACA-VERIGY-DPS-COM-E700266704-E700266404", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-AMOSTRADOR-AUTOMÁTICO-DIONEX-AS40-ASMAS40IB-03774304-PARA-PLACA-TRANS-COM-CABO-DE-FITA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-THERMO-SCIENTIFIC-DIONEX-2218161009R-ICS3000CPU", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-CONTROLE-DE-BANDEJA-THERMO-AND-DIONEX-PCB-AS50-PELTIER-AMOSTRADOR-AUTOMÁTICO-DRV-PN-049827", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-PEÇA-PLACA-DE-CIRCUITO-USADA-EMERSON-UT65-ISS-02.0070041064", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-PLACA-DE-CONTROLE-DE-CIRCUITO-USADA-EMERSON-TRANE-X1365087702", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-CONTROLADORA-PRINCIPAL-EMERSON-LIEBERT-0279556010-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-PLACA-DE-INTERFACE-DE-PLOTAGEM-LECO-DMA-777148C-XY-MAC400-CONTROLE-DE-FORNO-777149C-PC", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-PLACA_DE_FORMATURA_LECO_775910C_64K_777427", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-PLACA-DE-FORMATURA-LECO-775910C-65K-MAC400-CONTROLE-DE-FORNO-777130-PLACA-PLC-PC-B-PCB", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-25252-THERMO-CIENTÍFICA-PLACA-DE-CIRCUITO-IMPRESSO-ASSY-01X595204-84X595104-01X595201", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "CONCERTO-CROMATOGRAFOS-27508-THERMO-FISHER-SCIENTIFIC-PLACA-DE-CIRCUITO-IMPRESSO-TNG-TRANSPORTADORA-BD-COM-8000061010R-8000061000R", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-AGILENTHP-10544A-CRISTAL-OSCILADOR-10-MHZ-COM-BASE-DE-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-19624-AGILENT-PCB-PLACA-DE-PINOS-335013-E312626611-E312666611", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-34456-AGILENT-PCB-PLACA-VERIGY-DPS-COM-E700266704-E700266404", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-THERMO-SCIENTIFIC-DIONEX-2218161009R-ICS3000CPU", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-CONTROLE-DE-BANDEJA-THERMO-AND-DIONEX-PCB-AS50-PELTIER-AMOSTRADOR-AUTOMÁTICO-DRV-PN-049827", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-PEÇA-PLACA-DE-CIRCUITO-USADA-EMERSON-UT65-ISS-02.0070041064", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-PLACA-DE-CONTROLE-DE-CIRCUITO-USADA-EMERSON-TRANE-X1365087702", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-CONTROLADORA-PRINCIPAL-EMERSON-LIEBERT-0279556010-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-PLACA-DE-INTERFACE-DE-PLOTAGEM-LECO-DMA-777148C-XY-MAC400-CONTROLE-DE-FORNO-777149C-PC", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-MÓDULO-DE-PLACA-DE-CIRCUITO-PCB-YOKOGAWA-NP53BS9360AQ02", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-PLACA-DE-CIRCUITO-YOKOGAWA-B9628-LA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "MANUTENCAO-CROMATOGRAFOS-SHIMADZU-SWUNIDADE-14A-2213177191-PLACA-DE-PLACA-DE-CIRCUITO-IMPRESSO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-AGILENTHP-10544A-CRISTAL-OSCILADOR-10-MHZ-COM-BASE-DE-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-19624-AGILENT-PCB-PLACA-DE-PINOS-335013-E312626611-E312666611", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-THERMO-SCIENTIFIC-DIONEX-2218161009R-ICS3000CPU", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-CONJUNTO-DE-PLACA-CONTROLADORA-PRINCIPAL-EMERSON-LIEBERT-0279556010-PLACA-DE-CIRCUITO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-PLACA-DE-PCB-SHIMADZU-34589955F-34589870C", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-SHIMADZU-SPD6A-SUBSTITUIÇÃO-MONTAGEM-DE-PLACAS-DE-CIRCUITO-ASSY-PART-22817113B-PB3", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-SHIMADZU-SWUNIDADE-14A-2213177191-PLACA-DE-PLACA-DE-CIRCUITO-IMPRESSO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-SCIEX-025551-CONTROLE-DE-TEMPERATURA-PCB-API-3200-ESPECTRÔMETRO-MDS-FUNCIONANDO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-SCIEX-1016223-ESPECTRÔMETRO-PCB-CARD-APPLIED-BIOSYSTEMS-1029466-MDS-WORKING", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-SCIEX-5013979-CONTROLLER-BOARD-PLACA-DE-CIRCUITO-IMPRESSO-5013519-API-3200-SPECTROMETER-MDS-FUNCIONANDO", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "REPARO-CROMATOGRAFOS-CARTÃO-PCB-YOKOGAWA-CT5TKA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-34456-AGILENT-PCB-PLACA-VERIGY-DPS-COM-E700266704-E700266404", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-AMOSTRADOR-AUTOMÁTICO-DIONEX-AS40-ASMAS40IB-03774304-PARA-PLACA-TRANS-COM-CABO-DE-FITA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-CONJUNTO-DE-PLACA-THERMO-SCIENTIFIC-DIONEX-2218161009R-ICS3000CPU", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-CONTROLE-DE-BANDEJA-THERMO-AND-DIONEX-PCB-AS50-PELTIER-AMOSTRADOR-AUTOMÁTICO-DRV-PN-049827", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-PLACA-DE-PCB-SHIMADZU-34589955F-34589870C", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-SHIMADZU-SPD6A-SUBSTITUIÇÃO-MONTAGEM-DE-PLACAS-DE-CIRCUITO-ASSY-PART-22817113B-PB3", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-CARTÃO-PCB-YOKOGAWA-CT5TKA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},
    {"titulo": "ASSISTENCIA-TECNICA-CROMATOGRAFOS-PLACA-DE-CIRCUITO-YOKOGAWA-B9628-LA", "conteudo": "<h1>Fale Conosco</h1><p>Assistencia Técnica em Cromatografia.</p>"},

    
]

# Criar cada página da lista
for pagina in paginas:
    criar_pagina(pagina["titulo"], pagina["conteudo"])
