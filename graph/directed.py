def dg(u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph[u]:
     graph[u].append(v)

    
graph={}
dg(0,1)
dg(0,2)
dg(2,1)
dg('a' , 's')
dg('a' , 'a')
dg('a' , 'a')
dg(2,2)
dg(2,2)
# print(graph)
for key,value in graph.items():
    print(f"{key} --> {value}")