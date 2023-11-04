import networkx as nx

# Carregar o grafo a partir do arquivo GraphML
G = nx.read_graphml("grafo.graphml")

# Imprimir os nós e suas arestas
for node in G.nodes:
    print("Nó:", node)
    print("Vizinhos:", list(G.neighbors(node)))
    print()

# Imprimir as arestas
print("Arestas:")
for edge in G.edges:
    print(edge)

# Imprimir informações sobre o grafo
print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
