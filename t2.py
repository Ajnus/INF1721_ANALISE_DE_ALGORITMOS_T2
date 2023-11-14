import random
import math
import itertools
import networkx as nx
from collections import deque



#------------------------------------------------------ Tarefa 1 ----------------------------------------------------------

GRAFO_PATH = "/media/ajna/A6DE9820DE97E6B9/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml"

# retorna um hash da configuração recebida
def hash_cfg(cfg):
    return ''.join(str(x) for x in cfg)

# retorna a configuração do hash recebido
def unhash_cfg(hash_cfg):
    cfg = []
    for char in hash_cfg:
        cfg.append(int(char))
    return cfg

# "uma tabela hash H" 
H = {}

# "que dada configuração cfg, "H[cfg]" retorna o número do nó relativo a essa configuração"
def get_u(cfg):
    return H.get(hash_cfg(cfg), None)

# " nó:config, que será usada na BFS
H_Inversa = {}

# "um vetor C" 
C = []

# "que dado o número u de um nó, C[u] retorna a configuração correspondente a esse nó"
def get_cfg(u):
    cfg = C[u]
    if cfg is not None:
        return [int(x) for x in cfg]
    else:
        return None
    

# adiciona um nó com dada configuração ao grafo
def add_no(cfg, u):
    H[cfg] = u
    H_Inversa[u] = hash_cfg(cfg) # print adicional desnecessário
    print(f"    Item (Configuração:Nó) '{cfg}':{u} adicionado à tabela H.    ", end="")

# Dicionário para armazenar os vizinhos de cada nó
node_neighbors = {}

# adiciona um nó com dada configuração ao grafo
def add_vizinhos(u, vizinho):
    if u not in node_neighbors:
        node_neighbors[u] = []
    
    if isinstance(vizinho, list):
        node_neighbors[u].extend(vizinho)
        #print(f"Arestas ({u},{vizinho}) serão adicionadas")
    else:
        node_neighbors[u].append(vizinho)
        #print(f"Aresta ({u},{vizinho}) será adicionada")


# Testando as funções/criando UM grafo (com random seed, demorou mais de 4 milhões de iterações para criar todos os nós. abandonada)
cfg_numeros = [0,1,2,3,4,5,6,7,8]
print(f"len de cfg_numeros: {len(cfg_numeros)}")
nos_possiveis = math.factorial(len(cfg_numeros))
print(f"nos_possiveis: {nos_possiveis}\n")
# sendo 0 a casa vazia, apenas base. será embaralhada logo no início da iteração e só depois adicionada.



# # Criar/ler efetivamente o grafo
grafo = nx.read_graphml(GRAFO_PATH) 
print(f"grafo.number_of_nodes: {grafo.number_of_nodes()}")
#nx.draw(grafo, with_labels=True)

# Obter o primeiro nó do grafo
not_cfg_no_inicial = list(grafo.nodes)[0]

# Obter a configuração do primeiro nó
lstr_cfg_no_inicial = list(grafo.nodes[not_cfg_no_inicial]["config"])
cfg_no_inicial = [int(x) for x in lstr_cfg_no_inicial]

#print(f"AQUI: {hash_cfg(cfg_no_inicial)} {type(cfg_no_inicial)} {cfg_no_inicial[0]} {type(cfg_no_inicial[0])}")

# Criando nós em tempo linear
#perm = list(itertools.permutations(cfg_no_inicial, len(cfg_no_inicial)))

#node_numbers = []
#nodes_configurations=[]

#print(grafo.nodes)

for node_id in grafo.nodes():
    print("     ")
    #print(f"node: {node_id} type(node): {type(node_id)}")
    # Obter o número do nó
    node_number = int(node_id)

    # Obter a configuração do nó
    configuration = grafo.nodes[node_id]["config"]

    # adiciona configuração com seu respectivo nó à tabela H
    add_no(configuration, node_number)

    # Adicionar a configuração à lista configurations
    C.append(configuration)
    
"""
t=0
for c in perm:
    print(f"c: {c} type(c): {type(c)}")
    print("start")

    # Obter o número do nó
    node_number = perm.index(c)

    print(c)

    # Obter a configuração do nó
    configuration = list(c)

    # # adiciona nó com sua configuração à tabela H
    add_no(node_number, configuration)

    # Adicionar a configuração à lista configurations
    C.append(configuration)

    #if t%2!=0:
    #    print(" ")
    #t+=1
"""



# 1. Quantos nós e aresta existem no grafo do espaço de estados que você construiu

# Dado "1) um nó para cada configuração possı́vel do tabuleiro;": a casa vazia pode estar em 9 posições diferentes e as preenchidas podem ser ocupadas por 8 números diferentes. Logo o número total de nós/configurações possíveis NO JOGO é de 9 * 8! = 362.880.
# (que é igual a 9!) 

# Já o número de arestas depende de qual é a configuração/estado inicial do jogo. Nem todos os estados/nós existentes são atingíveis a partir de um dado estado inicial, independente do número de movimentos totais no jogo.

# Desta forma para determinar as arestas existentes precisamos a partir de todos os nós possíveis gerados no grafo filtrar os antigíveis e não atingíveis a partir do nó inicial.



# Retorna lista com estados vizinhos de um dado estado
def get_neighbors(config):
    config_ = [int(x) for x in config]  # Converter a configuração para uma lista de inteiros
    neighbors_config = []
    casa_vazia = config_.index(0)                                # pega a posição da casa vazia
    
    """
    nova solução mais eficiente mas não o bastante, abandonada
    if casa_vazia == 0:
        neighbor = list(config)
        neighbor2 = list(config)

        neighbor[0], neighbor[1] = neighbor[1], neighbor[0]
        neighbors_config.append(neighbor)

        neighbor2[0], neighbor2[4] = neighbor2[4], neighbor2[0]
        neighbors_config.append(neighbor2)  

    elif casa_vazia == 1:
        neighbor = list(config)
        neighbor2 = list(config)
        neighbor3 = list(config)

        neighbor[1], neighbor[0] = neighbor[0], neighbor[1]
        neighbors_config.append(neighbor)

        neighbor2[1], neighbor2[2] = neighbor2[2], neighbor2[1]
        neighbors_config.append(neighbor2)

        neighbor3[1], neighbor3[4] = neighbor3[4], neighbor3[1]
        neighbors_config.append(neighbor3)

    elif casa_vazia == 2:
        neighbor = list(config)
        neighbor2 = list(config)

        neighbor[2], neighbor[1] = neighbor[1], neighbor[2]
        neighbors_config.append(neighbor)

        neighbor2[2], neighbor2[5] = neighbor2[5], neighbor2[2]
        neighbors_config.append(neighbor2)

    elif casa_vazia == 3:
        neighbor = list(config)
        neighbor2 = list(config)
        neighbor3 = list(config)

        neighbor[3], neighbor[0] = neighbor[0], neighbor[3]
        neighbors_config.append(neighbor)

        neighbor2[3], neighbor2[4] = neighbor2[4], neighbor2[3]
        neighbors_config.append(neighbor2)  

        neighbor3[3], neighbor3[6] = neighbor3[6], neighbor3[3]
        neighbors_config.append(neighbor3)  

    elif casa_vazia == 4:
        neighbor = list(config)
        neighbor2 = list(config)
        neighbor3 = list(config)
        neighbor4 = list(config)

        neighbor[4], neighbor[1] = neighbor[1], neighbor[4]
        neighbors_config.append(neighbor)

        neighbor2[4], neighbor2[3] = neighbor2[3], neighbor2[4]
        neighbors_config.append(neighbor2)

        neighbor3[4], neighbor3[7] = neighbor3[7], neighbor3[4]
        neighbors_config.append(neighbor3)

        neighbor4[4], neighbor4[5] = neighbor4[5], neighbor4[4]
        neighbors_config.append(neighbor4)

    elif casa_vazia == 5:
        neighbor = list(config)
        neighbor2 = list(config)
        neighbor3 = list(config)

        neighbor[5], neighbor[2] = neighbor[2], neighbor[5]
        neighbors_config.append(neighbor)

        neighbor2[5], neighbor2[4] = neighbor2[4], neighbor2[5]
        neighbors_config.append(neighbor2)

        neighbor3[5], neighbor3[8] = neighbor3[8], neighbor3[5]
        neighbors_config.append(neighbor3)

    elif casa_vazia == 6:
        neighbor = list(config)
        neighbor2 = list(config)

        neighbor[6], neighbor[3] = neighbor[3], neighbor[6]
        neighbors_config.append(neighbor)

        neighbor2[6], neighbor2[7] = neighbor2[7], neighbor2[6]
        neighbors_config.append(neighbor2)

    elif casa_vazia == 7:
        neighbor = list(config)
        neighbor2 = list(config)
        neighbor3 = list(config)

        neighbor[7], neighbor[6] = neighbor[6], neighbor[7]
        neighbors_config.append(neighbor)

        neighbor2[7], neighbor2[4] = neighbor2[4], neighbor2[7]
        neighbors_config.append(neighbor2)  

        neighbor3[7], neighbor3[8] = neighbor3[8], neighbor3[7]
        neighbors_config.append(neighbor3)

    elif casa_vazia == 8:
        neighbor = list(config)
        neighbor2 = list(config)

        neighbor[8], neighbor[7] = neighbor[7], neighbor[8]
        neighbors_config.append(neighbor)

        neighbor2[8], neighbor2[5] = neighbor2[5], neighbor2[8]
        neighbors_config.append(neighbor2)  
    
    neighbors = []"""

    # Define as posições válidas para a casa vazia trocar de lugar
    valid_swaps = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

    # Gera os vizinhos trocando a casa vazia com peças adjacentes
    for neighbor_index in valid_swaps[casa_vazia]:
        neighbor = config_.copy()  # Cria uma cópia da configuração atual
        neighbor[casa_vazia], neighbor[neighbor_index] = neighbor[neighbor_index], neighbor[casa_vazia]
        neighbors_config.append(neighbor)

    return neighbors_config

# efetua uma troca entre peças, o que é proibido no jogo logo estados não conectados por arestas
def troca_proibida(config):
    casa_preenchida1 = config.index(5) 
    casa_preenchida2 = config.index(4) 

    config_proibida = list(config)
    config_proibida[casa_preenchida1], config_proibida[casa_preenchida2] = config_proibida[casa_preenchida2], config_proibida[casa_preenchida1]

    return config_proibida


print(f"\nNó 0 inicial: {hash_cfg(cfg_no_inicial)}\nSeus nós vizinhos (contém arestas entre si): {get_neighbors(hash_cfg(cfg_no_inicial))}")
print(f"Nós que não contém arestas entre si: {cfg_no_inicial} e {troca_proibida(cfg_no_inicial)}")



#------------------------------------------------------ Tarefa 2 ----------------------------------------------------------
qtd_camadas="" # adicional para a Tarefa 3
mais_distantes=[] # adicional para a Tarefa 3
num_componentes=0

def BFS(grafo, no_inicial, visitados, do_print):
    global num_arestas
    global mais_distantes
    global qtd_camadas

    L=[]
    L.append([no_inicial])

    if do_print == True:
        print(f"\nNó inicial: {no_inicial}\n---")

    visitados[no_inicial] = True
    pai = {no_inicial: None}
    if do_print == True:
        print("\n", end="")

    i=1
    while i <= len(L):    # quantidade de camadas nunca vai ultrapassar a quantidade de nós
        if do_print == True:
            print(f"\ni: {i}")

        L.append([])
        #L[i]   # level i
        if do_print == True:
            print(f"L: {L}\n")

        for u in L[i-1]:
            u_neighbors = get_neighbors(get_cfg(int(u)))
            
            
            for vizinho_cfg in u_neighbors:
                vizinho_u = get_u(vizinho_cfg)
                if vizinho_u not in visitados or not visitados[vizinho_u]:

                    L[i].append(vizinho_u)
                    add_vizinhos(u, vizinho_u) # adicional para a Tarefa 3
                    num_arestas+=1

                    pai[vizinho_u] = u
                    visitados[vizinho_u] = True

        if L[i]==[]:
            qtd_camadas = i-1
            if do_print == True:
                print(f"Camadas: {qtd_camadas}")
            mais_distantes = L[i-1] # adicional para a Tarefa 3, pega os nós da camada anterior
            return
        
        i+=1


def BFS_componentes(grafo):
    visitados = {node: False for node in grafo}
    global num_componentes

    print("\n", end="")
    for s in grafo:
        #print(f"s: {s}")
        if not visitados[s]:
            BFS(grafo, s, visitados, True)
            num_componentes+=1

            #print(f"\nTotal de nós visitados no momento da iteração {num_componentes}:")
            k=0
            for s in grafo:
                
                if visitados[s] == True:
                    k+=1
                    #print(f"{s}, ", end="")  
            print(f"\n\nQuantidade total de nós visitados no momento da iteração {num_componentes}: {k}\n---")

    print("\nQuantidade total de componentes conexas:", num_componentes)



num_arestas=0
visitados = {node: False for node in H_Inversa}
BFS_componentes(H_Inversa) #  utilizada pois é a de item node_number:cfg
print(f"\nO numero de arestas do grafo é: {num_arestas}")
print(f"\nO u dos nós mais distantes do são: {mais_distantes}")


#------------------------------------------------------ Tarefa 3 ----------------------------------------------------------

cfg_no_final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

"""
def BFS_com_caminho(grafo, s, target):
    visitados = set()
    queue = [(s, [s])]
    while queue:
        (no_atual, caminho) = queue.pop(0)
        print(f"no_atual: {no_atual}, target: {target}")

        if no_atual == target:
            print(f"no_atual == target! {no_atual} == {target} | caminho: {caminho}")
            return caminho
        
        if no_atual not in visitados:
            visitados.add(no_atual)
            vizinhos = node_neighbors.get(int(no_atual), [])
            #print(f"no_atual: {no_atual}, target: {target}, caminho: {caminho}, vizinhos: {vizinhos}")
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    queue.append((vizinho, caminho + [vizinho]))
    return []

for s in grafo:
    BFS_com_caminho(H_Inversa, s, get_u(cfg_no_final))
"""

# Respostas
visitados = {node: False for node in H_Inversa}
BFS(H_Inversa, get_u(cfg_no_final), visitados, False) # alternativa mais simples, seta mais_distantes do nó final
print("\nPossibilidades equidistantes de configuração inicial viável mais difícil de alcançar (configuração dos nós acima):")
for md in mais_distantes:
    print(get_cfg(md))
print("Quantidade de movimentos necessários:", qtd_camadas)
