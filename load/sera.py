import networkx as nx

# Carregar o grafo a partir do arquivo GraphML
G = nx.read_graphml("grafo.graphml")

# Ler o conteúdo do arquivo "output.txt"
with open("output.txt", "r") as file:
    output_content = file.readlines()[362888:424555]  # Lê do arquivo da linha 362886 até a linha 825956

# Dicionário para armazenar os vizinhos de cada nó
node_neighbors = {}

# Variáveis para armazenar o nó atual e seus vizinhos
current_node = None
current_node_neighbors = []

# Analisar o conteúdo do arquivo
for index, line in enumerate(output_content):
    line = line.strip()

    if line.startswith("Nó"):
        # Imprimir o nó anterior e seus vizinhos, se houver
        if current_node and current_node_neighbors:
            node_neighbors[current_node] = current_node_neighbors
            current_node_neighbors = []

        # Obter o identificador do novo nó
        current_node = int(line.split()[1][:-1])  # Remover os dois pontos ":" do final do identificador

    elif line.startswith("Vizinhos"):
        # Obter os vizinhos do nó
        #neighbors_line=[]
        i=0
        while ((output_content[index + 1+i].startswith("aresta") == False) and (output_content[index  +1+i].strip() != "")):
            current_node_neighbors.append(output_content[index + 1+i].strip()[:-1])
            i+=1

        print(f"current_node_neighbors: {current_node_neighbors}")

        #if neighbors_line:
            #neighbors = neighbors_line.split(", ")
        #    current_node_neighbors = [neighbor for neighbor in neighbors_line]
        #    print(f"current_node_neighbors: {current_node_neighbors}, current_node_neighbors type: {type(current_node_neighbors[0])})")
            

# Adicionar os vizinhos do último nó
if current_node and current_node_neighbors:
    node_neighbors[current_node] = current_node_neighbors

# Criar arestas entre os vizinhos
for node, neighbors in node_neighbors.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Imprimir os nós e seus vizinhos
for node, neighbors in node_neighbors.items():
    print(f"Nó {node} tem como vizinhos:")
    for neighbor in neighbors:
        print(f" - Nó {neighbor}")
    print()

# Salvar as alterações no arquivo GraphML
nx.write_graphml(G, "grafo.graphml")

# Imprimir informações sobre o grafo
print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
