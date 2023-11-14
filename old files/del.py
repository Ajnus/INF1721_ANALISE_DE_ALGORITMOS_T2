filename = "/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml"  # substitua pelo caminho do seu arquivo

# Ler o conteúdo do arquivo
with open(filename, "r") as file:
    lines = file.readlines()

# Verificar se o arquivo possui pelo menos 1088643 linhas
if len(lines) > 1088643:
    # Substituir o conteúdo do arquivo pelas primeiras 1088643 linhas
    lines = lines[:1088643]

    # Sobrescrever o arquivo com as linhas atualizadas
    with open(filename, "w") as file:
        file.writelines(lines)
        file.truncate()

    print("Linhas após a linha 1088643 deletadas com sucesso.")
else:
    print("O arquivo não possui 1088643 linhas ou mais.")

