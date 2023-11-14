# Abrir o arquivo de entrada para leitura
with open("/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml", "r") as input_file:
    # Ler todas as linhas do arquivo
    all_lines = input_file.readlines()

    # Encontrar a primeira ocorrência de 'oi'
    start_index = next((i for i, line in enumerate(all_lines) if "oi" in line), None)

    if start_index is not None:
        # Encontrar a próxima ocorrência de 'oi' após a primeira
        end_index = next((i for i, line in enumerate(all_lines[start_index+1:]) if "oi" in line), None)
        end_index = end_index + start_index + 1 if end_index is not None else len(all_lines)

        # Recortar as linhas desejadas
        cut_lines = all_lines[start_index:end_index]

        # Excluir as linhas recortadas do arquivo original
        del all_lines[start_index:end_index]

        # Abrir o arquivo de saída para escrita
        with open("outnodes.txt", "w") as output_file:
            # Escrever as linhas recortadas no arquivo de saída
            output_file.writelines(cut_lines)

        # Sobrescrever o arquivo original sem as linhas recortadas
        with open("/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml", "w") as input_file:
            input_file.writelines(all_lines)

        print("Recorte concluído. O conteúdo foi salvo em 'outnodes.txt' e removido de 'grafo.graphml'.")
    else:
        print("A palavra oi não foi encontrada no arquivo 'grafo.graphml'.")
