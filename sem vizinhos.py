import networkx as nx

# Load the graph from a GraphML file
graph_file = "/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml"
grafo = nx.read_graphml(graph_file)


# retorna um hash da configuração recebida
def hash_cfg(cfg):
    return ''.join(str(x) for x in cfg)

# "uma tabela hash H" 
H = {}


# adiciona um nó com dada configuração ao grafo
def add_no(u, cfg):
    H[u] = hash_cfg(cfg)
    #print(f"    Nó {u} adicionado à tabela, com configuração {H[u]}    ", end="")

# "um vetor C" 
C = []

# "que dado o número u de um nó, C[u] retorna a configuração correspondente a esse nó"
def get_cfg(u):
    #print(f"u: {u} type(u): {type(u)}")
    cfg = C[u]
    if cfg is not None:
        return [int(x) for x in cfg]
    else:
        return None
        

for node in grafo.nodes:
    #print("start")
    # Obter o número do nó
    node_number = int(node)

    if node_number == 362879:
        # Obter a configuração do nó
        configuration = grafo.nodes[node]["config"]

        # adiciona nó com sua configuração à tabela H
        add_no(node_number, configuration)

        # Adicionar a configuração à lista configurations
        C.append(configuration)
        break

    # Obter a configuração do nó
    configuration = grafo.nodes[node]["config"]

    # # adiciona nó com sua configuração à tabela H
    add_no(node_number, configuration)

    # Adicionar a configuração à lista configurations
    C.append(configuration)        

## Find nodes with less than two neighbors
nodes_with_less_than_two_neighbors = []
for node in grafo.nodes():
    neighbors = list(grafo.neighbors(node))
    if len(neighbors) < 2:
        nodes_with_less_than_two_neighbors.append(node)

# Display the nodes with less than two neighbors
for node in nodes_with_less_than_two_neighbors:
    print(node)
