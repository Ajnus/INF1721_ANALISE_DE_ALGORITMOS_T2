import networkx as nx

# Carregar o grafo a partir do arquivo GraphML
G = nx.read_graphml("grafo.graphml")

# Imprimir informações sobre o grafo
print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
print("Nós do grafo:", G.nodes())
print("Arestas do grafo:", G.edges())

# Imprimir o grafo na tela
print("Grafo:")
for node in G.nodes():
    print(f"Nó {node}: {G.nodes[node]['config']}")

