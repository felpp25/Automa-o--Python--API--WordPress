palavras_chave = [
    "CONSERTOS-DE-TRANSDUTORES-MÉDICOS",
    "MANUTENCAO-DE-TRANSDUTORES-MÉDICOS",
    "REPARO-DE-TRANSDUTORES-MÉDICOS",
    "ASSISTENCIA-TECNICA-DE-TRANSDUTORES-MÉDICOS"
]

modelos = [
    "TRANSESOFÁGICO",
    "CÁRDIO",
    "CONVEXOS-E-MICROCONVEXOS",
    "LINEARES",
    "GOIÂNIA",
    "GOIÁS",
    "BRASIL"
    "ATENDIMENTO-NACIONAL",
    "PEÇAS-ORIGINAIS",
    "TROCA-DE-CRISTAIS",
    "TRANSDUTORES-COM-GARANTIA",
    "TRANSDUTORES-ORIGINAIS",
    "TRANSDUTOR-COM-DEFEITO"
]

# Gerando e salvando no arquivo .txt
with open("tags_cromatografos.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras_chave:
        for modelo in modelos:
            arquivo.write(f"{palavra}-{modelo}\n")

print("Arquivo 'tags_transdutores.txt' gerado com sucesso!")
