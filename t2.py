import random
import math
import itertools
import networkx as nx

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
def get_u( cfg):
    #print(f"[GET_U]cfg: {cfg}")

    for u in H:
        #print(f"u, config: {u}, {cfg}")
        if 'config' in H[u]:
            #config = H[u]['config']
            #print(f"H[u]: {u}")
            if hash_cfg(cfg) == H[u]['config']:
                return u

    #print(f"H[6]['config']: {H[6]['config']}")
    #print(f"{hash_cfg(cfg)} != {H[6]['config']}")
    return None


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
    

# adiciona um nó com dada configuração ao grafo
def add_no(u, cfg):
    H[u] = {'config': hash_cfg(cfg), 'vizinhos': []}
    print(f"    Nó {u} adicionado à tabela, com configuração {H[u]['config']}    ", end="")

# adiciona um nó com dada configuração ao grafo
def add_vizinhos(u, vizinho):
    if 'vizinhos' not in H[u]:
        H[u]['vizinhos'] = []

    H[u]['vizinhos'].extend(vizinho)
    #print(f"    Vizinho {get_u( vizinho)} adicionados à tabela, com configuração {vizinho}    ", end="")
    print(f"aresta {u}: {get_u(vizinho)} adicionada")

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

print(f"AQUI: {cfg_no_inicial} {type(cfg_no_inicial)} {cfg_no_inicial[0]} {type(cfg_no_inicial[0])}")

# Imprimir a configuração do primeiro nó
#print("Configuração do primeiro nó:")
#for attribute, value in cfg_no_inicial.items():
#    print(f"{attribute}: {value}")

#random.shuffle(cfg_numeros)
#cfg_no_inicial = cfg_numeros.copy()                     # registrado para mais tarde
#print(f"Iteração 1: ", end="")
#add_no(0, cfg_no_inicial)                               # adiciona nó inicial à tabela H
#C.append(cfg_no_inicial.copy())                         # adiciona cfg inicial ao vetor C
#print(f"Nó 0: {cfg_no_inicial}")                       # imprime nó e estado/cfg, inicial

#print(f"    Nós criados: {len(H)}")


#i=1
#j=1
#t=0
#while i < nos_possiveis:          # 1) um nó para cada configuração possı́vel do tabuleiro;
#    t+=1
#    print(f"Iteração {t+1}: ", end="")
    #print(f"i inicial: {i}")
    #random.shuffle(cfg_numeros)
 #   valor_hash = hash_cfg(cfg_numeros)

    #print(f"len(H): {len(H)}")
    #print(f"nos_possiveis: {nos_possiveis}")

  #  if valor_hash not in H.values() and len(H) <= nos_possiveis:                    # se nó com esta configuração já não existir        
   #     add_no(j, cfg_numeros)                          # adiciona nó à tabela H
    #    C.append(cfg_numeros.copy())                    # adiciona cfg ao vetor C
        #print(f"Nó {j}: {C[-1]}")                       # imprime nó e estado/cfg, poderia também ser mostrado o hash através de hash_cfg(get_cfg(j))
     #   j+=1                                            # número real de configurações/nós

    #else:
     #   existing_node = [u for u, cfg in H.items() if cfg == valor_hash][0]         # determina em que Nó a configuração já existe
      #  print(f"    {valor_hash}: configuração já existe no Nó {existing_node}           ", end="")  # imprimindo logo em seguida
        #print(f"i: {i}")
       # i-=1                                                                       # garante que TODOS os nós possíveis sejam criados
        #print(f"i depois de i--: {i}")
    
    #print(f"    Nós criados: {len(H)}")
    #i+=1


#print (f"\nTotal de {j} nós no grafo.")
#print(f"Total de {t+1} iterações para criar todos os seus nós.\n")


# Criando nós em tempo linear
#perm = list(itertools.permutations(cfg_no_inicial, len(cfg_no_inicial)))

#node_numbers = []
#nodes_configurations=[]

for node in grafo.nodes:
    print("start")
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
    

#t=0
#for c in perm:

#    C.append(c)
#    if t%2!=0:
#        print("\n")
#    t+=1



# 1. Quantos nós e aresta existem no grafo do espaço de estados que você construiu

# Dado "1) um nó para cada configuração possı́vel do tabuleiro;": a casa vazia pode estar em 9 posições diferentes e as preenchidas podem ser ocupadas por 8 números diferentes. Logo o número total de nós/configurações possíveis NO JOGO é de 9 * 8! = 362.880.
# (que é igual a 9!) 

# Já o número de arestas depende de qual é a configuração/estado inicial do jogo. Nem todos os estados/nós existentes são atingíveis a partir de um dado estado inicial, independente do número de movimentos totais no jogo.

# Desta forma para determinar as arestas existentes precisamos a partir de todos os nós possíveis gerados no grafo filtrar os antigíveis e não atingíveis a partir do nó inicial.

# Retorna lista com estados vizinhos de um dado estado
def get_neighbors(config):
    neighbors_config = []
    casa_vazia = config.index(0)                                # pega a posição da casa vazia
    

    if casa_vazia >= 3:                                         # Peça pra baixo se possível
        # peça 'troca de posição' com casa vazia
        neighbor = list(config)
        neighbor[casa_vazia], neighbor[casa_vazia-3] = neighbor[casa_vazia-3], neighbor[casa_vazia]
        neighbors_config.append(neighbor)                       # adiciona nó/estado vizinho

    if casa_vazia <= 5:                                         # Peça pra cima se possível
        neighbor = list(config)
        neighbor[casa_vazia], neighbor[casa_vazia+3] = neighbor[casa_vazia+3], neighbor[casa_vazia]
        neighbors_config.append(neighbor)
    
    if casa_vazia != 2 and casa_vazia != 5 and casa_vazia != 8:   # Peça pra esquerda se possível
        neighbor = list(config)
        neighbor[casa_vazia], neighbor[casa_vazia+1] = neighbor[casa_vazia+1], neighbor[casa_vazia]
        neighbors_config.append(neighbor)
    
    if casa_vazia != 0 and casa_vazia != 3 and casa_vazia != 6:   # Peça pra direita se possível
        neighbor = list(config)
        neighbor[casa_vazia], neighbor[casa_vazia-1] = neighbor[casa_vazia-1], neighbor[casa_vazia]
        neighbors_config.append(neighbor)

    return neighbors_config

def troca_proibida(config):
    casa_preenchida1 = config.index(5) 
    casa_preenchida2 = config.index(4) 

    config_proibida = list(config)
    config_proibida[casa_preenchida1], config_proibida[casa_preenchida2] = config_proibida[casa_preenchida2], config_proibida[casa_preenchida1]

    return config_proibida

#print(f"Tabela H:\nH[6]['config'] : {H[6]['config']}")

#num_arestas=0

#for u in H:
    #print(f"{H[u]['config']}")
#    cfg = (H[u]['config'])
#    cfg_vizinhos = get_neighbors(unhash_cfg(cfg))
#    print(f"\n\nNó {u}: {unhash_cfg(cfg)}\nSeus nós vizinhos (conectados por uma aresta): {cfg_vizinhos}")
#    for cfg_vizinho in cfg_vizinhos:
        #print(f"cfg_vizinho: {cfg_vizinho}, type {type(cfg_vizinho[0])}")
#        print(f"{get_u(cfg_vizinho)}, ", end="")
#        no_vizinhos.add(get_u( hash_cfg(cfg_vizinho)))
#        print("")

#    for cfg_vizinho in cfg_vizinhos:
        #print(f"cfg_vizinho: {cfg_vizinho}")
        # Verifica se a chave já existe na tabela hash
#        if u in H:
            # Se a chave existir, adiciona o vizinho à lista de vizinhos do nó
#            add_vizinhos(u, cfg_vizinho)

#            num_arestas+=1
        #else:
            # Se a chave não existir, cria uma nova lista com o valor e atribui à chave
            #H[u] = [cfg_vizinho]
            #print(f"aresta {u}: {get_u( cfg_vizinho)} criada")



#file_path = "/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/sem vizinhos.txt"
#elements = []

#with open(file_path, "r") as file:
    #for line in file:
        #values = line.split()  # Separa os valores da linha
        #values = [int(value.replace(",", "").replace("[", "").replace("]", "")) for value in values]  # Remove as vírgulas dos valores
        #vector = [int(value) for value in values]  # Converte os valores para inteiros
        #elements.append(values)  # Adiciona os valores ao vetor 'elements'
        
#print(f"sem vizinhos: {elements} {type(elements[0][0])}")

# Criar um iterador com os valores de H a partir do nó 143833
#it = itertools.islice(elements, 0, 460)

# Adicionar arestas entre todos os vizinhos
#for no_config in it:
    #print (get_u( no_config))
    #if get_u( no_config) < 142822:
    #    continue


#    no_vizinhos = set()
    
#    print (f"\n\nNó {get_u( no_config)}: {unhash_cfg(no_config)}")
#    cfg_vizinhos = get_neighbors((unhash_cfg(no_config)))  # Encontrar configs dos vizinhos do nó
#    print(f"Vizinhos: {cfg_vizinhos}")
#    for cfg_vizinho in cfg_vizinhos:
#        print(f"{get_u( cfg_vizinho)}, ", end="")
#        no_vizinhos.add(get_u( hash_cfg(cfg_vizinho)))
#        print("")

    #for no_vizinho in no_vizinhos:
                #if not grafo.has_edge(get_u( no_config), no_vizinho):  # Verifica se a aresta já existe
                #if not (str(no_vizinho) in H[get_u( no_config)]):
                    #print(f"get_u( no_config), no_vizinho: {get_u( no_config)}, {no_vizinho}")
                    #grafo.add_edge(get_u( no_config), no_vizinho)      # Traça aresta entre os vizinhos
                    #H[get_u( no_config)].append(no_vizinho)
                    #num_arestas+=1
                    #nx.write_graphml(grafo, "/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml") # Salvar as alterações no arquivo GraphML
                    #print(f"aresta {get_u( no_config), no_vizinho} salva")
        
#nx.write_graphml(grafo, "/home/puc/Documentos/PUC-Rio/INF1721 - Analise de Algoritmos/Trabalho 2/grafo.graphml") # Salvar as alterações no arquivo GraphML

#print(f"\nO numero de arestas do grafo é: {num_arestas}")
print(f"\nNó 0 inicial: {cfg_no_inicial}\nSeus nós vizinhos (contém arestas entre si): {get_neighbors(cfg_no_inicial)}")
print(f"Nós que não contém arestas entre si: {cfg_no_inicial} e {troca_proibida(cfg_no_inicial)}")


# Carregar o grafo a partir do arquivo GraphML
# Go = nx.read_graphml("meu_grafo.graphml")

# Exibir informações sobre o grafo
#for u, v in Go.edges():
#    print(f"Aresta: {u} - {v}")

#print("Número de nós:", Go.number_of_nodes())
#print("Número de arestas:", Go.number_of_edges())


#------------------------------------------------------ Tarefa 2 ----------------------------------------------------------

def BFS(grafo, no_inicial, visitados):
    global num_arestas
    #L=[None]*nos_possiveis           # quantidade de camadas nunca vai ultrapassar a quantidade de nós
    #print(f"L size: {len(L)}")
    L=[]
    L.append([no_inicial])
    #print(f"\n\nL: {L}\n")
    #print(f"L size: {len(L)}")
    print(f"\nNó inicial: {no_inicial}")
    #print(f"visitados? {visitados}")
    visitados[no_inicial] = True
    pai = {no_inicial: None}
    print("\n", end="")

    i=1
    while i <= len(L):    # quantidade de camadas nunca vai ultrapassar a quantidade de nós
        print(f"i: {i}")
        #print(f"nos_possiveis: {nos_possiveis}")
        L.append([])
        #L[i]   # level i
        print(f"L: {L}")
        #   print(f"L[{i}] = {L[i]}")
        for u in L[i-1]:
            #print(f"L[{i-1}]: {L[i-1]} ({type(L[i-1])})")
            #print(f"for u in L[i-1]:\n      u: {u} ({type(u)})")
            #print(f"int(u): {int(u)}")
            #print(f"get_cfg(int(u)): {get_cfg(int(u))}  ({get_cfg(int(type(u)))})")
            u_neighbors = get_neighbors(get_cfg(int(u)))
            #print(f"{u}_neighbors: {u_neighbors}")
            
            for vizinho_cfg in u_neighbors:
                #print(f"visitados: {visitados}")    
                #print(f"vizinho_cfg: {vizinho_cfg}")
                vizinho_u = get_u(vizinho_cfg)
                #print(f"vizinho_u: {vizinho_u}")
                if visitados[vizinho_u] == False:
                    #print(f"vizinho: {vizinho_u}")
                    #print(f"L[{i}] = {L[i]}")
                    L[i].append(vizinho_u)
                    num_arestas+=1
                    #print(f"L: {L}")
                    #print(f"int(get_u( vizinho)): {int(get_u( vizinho))}")
                    pai[vizinho_u] = u
                    visitados[vizinho_u] = True
                    #print(f"visitados[tuple(vizinho)]: {visitados[get_u( vizinho)]}")

            #print("saiu")
        if L[i]==[]:
            #print(f"L[{i}] = {L[i]}")
            #print("agora saiu memo")
            return
        i+=1


def BFS_componentes(grafo):
    visitados = {node: False for node in grafo}
    num_componentes=0

    print("\n", end="")
    for s in grafo:
        #print(f"s: {s}")
        if not visitados[s]:
            BFS(grafo, s, visitados)
            num_componentes+=1

                
            print(f"\nTotal de nós visitados no momento da iteração {num_componentes}:")
            k=0
            for s in grafo:
                
                if visitados[s] == True:
                    k+=1
                    print(f"{s}, ", end="")  
            print(f"\n\nQuantidade total de nós visitados no momento da iteração {num_componentes}: {k}\n---")

            

    
    print("\nQuantidade total de componentes conexas:", num_componentes)



num_arestas=0
visitados = {node: False for node in H}
BFS_componentes(H)
print(f"\nO numero de arestas do grafo é: {num_arestas}")

#------------------------------------------------------ Tarefa 3 ----------------------------------------------------------

def BFS_com_caminho(grafo, s, target):
    visitados = set()
    queue = [(s, [s])]
    while queue:
        (no_atual, caminho) = queue.pop(0)
        if no_atual == target:
            return caminho
        if no_atual not in visitados:
            visitados.add(no_atual)
            vizinhos = grafo[no_atual]
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    queue.append((vizinho, caminho + [vizinho]))
    return []

cfg_no_final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Acha o componente conexo que contém a configuração final cfg*
cconexa = []
for no in grafo:
    if BFS_com_caminho(grafo, no, cfg_no_final):
        cconexa.append(no)

# Acha a configuração inicial viável que necessita do maior número de movimentos
max_moves = 0
max_moves_config = None

for config in cconexa:
    caminho = BFS_com_caminho(grafo, cfg_no_final, config)
    if len(caminho) > max_moves:
        max_moves = len(caminho)
        max_moves_config = config

print("Configuração inicial viável mais difícil de alcançar:", max_moves_config)
print("Quantidade de movimentos necessários:", max_moves)




