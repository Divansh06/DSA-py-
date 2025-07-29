def directed_add_edges(u,v,w):
    if u not in graph:
        graph[u]=[]
    if (v,w) not in graph[u]:
        graph[u].append((v,w))


    
graph={}
directed_add_edges(0,1,2)
directed_add_edges(0,1,3)
directed_add_edges(0,2,1)
directed_add_edges(1,2,3)

# print(graph)
for key,value in graph.items():
    print(f"{key} --> {value}")