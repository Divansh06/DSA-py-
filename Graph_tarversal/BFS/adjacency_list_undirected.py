#undirected adjacency list.
graph ={}
def add_edge(u,v):
    if u not in graph:
        graph[u] = []
    if v not in graph[u]:
        graph[u].append(v)
    # as it is undirected so we need to define it both ways.
    if v not in graph:
        graph[v]=[]
    if u not in graph[v]:
        graph[v].append(u)

# BFS implementation    
from collections import deque

def bfs(start):
    visited =set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end =" ")
            visited.add(node)
        for neighbour in graph[node]:
            # print(neighbour)
            if neighbour not in visited:
                queue.append(neighbour)

# using function 
add_edge(2,6)
add_edge(2,5)
add_edge(1,4)
add_edge(0,2)
add_edge(1,3)
add_edge(0,1)

print("Adjacency list")
for key,value in graph.items():
    print(f"{key} --- {value}")

print("BFS")
bfs(0)


    
