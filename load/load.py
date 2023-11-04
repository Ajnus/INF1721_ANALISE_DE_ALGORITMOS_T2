import re
import networkx as nx

# Ler o conteúdo do arquivo de saída
with open("output.txt", "r") as file:
    output_content = file.readlines()[3:362882]  # Lê do arquivo da linha 4 até a linha 362882

# Criar um grafo vazio
G = nx.Graph()

# Adicionar nós ao grafo
for line in output_content:
    line = line.strip()
    node_info = re.findall(r'Nó (\d+)', line)
    node_configs = re.findall(r'configuração (.{9})', line)
    for i in range(min(len(node_info), len(node_configs))):
        node_id = int(node_info[i])
        node_config = node_configs[i].strip()
        G.add_node(node_id, config=node_config)

# Exemplo de uso do grafo
print("Número de nós:", G.number_of_nodes())
print("Nós do grafo:", G.nodes())

# Salvar o grafo em um arquivo
nx.write_graphml(G, "grafo.graphml")
print("Grafo salvo com sucesso no arquivo grafo.graphml")
