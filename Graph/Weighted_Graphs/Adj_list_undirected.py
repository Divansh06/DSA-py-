def add_undirected_edge(u,v,w):
    if u not in graph:
        graph[u] = []
    if v not in graph[u]:        # <-- avoids duplicate edge
        graph[u].append((v,w))

    if v not in graph:
        graph[v] = []
    if u not in graph[v]:        # <-- for undirected graph
        graph[v].append((u,w))

graph={}
add_undirected_edge(0,1,2)
add_undirected_edge(0,2,4)
add_undirected_edge(2,0,5)
add_undirected_edge(3,1,6)

for key,value in graph.items():
        print(f"{key} ---> {value}")

# print(f"{key} --->{' '.join(map(str,value))}")
    # print(f"{key} ---> {str(value)[1:-1]}")