def directed_add_edges(u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph[u]:
        graph[u].append(v)

    
graph={}
directed_add_edges(0, 1)
directed_add_edges(0, 1)
directed_add_edges(0, 2)
directed_add_edges(1, 2)
directed_add_edges(1, 2)
directed_add_edges(2, 0)
# print(graph)
for key,value in graph.items():
    print(f"{key} --> {value}")