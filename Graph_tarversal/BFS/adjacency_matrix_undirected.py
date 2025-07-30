# created matrix 
def create_mat(n,edges):
    adj_mat =[[0]*n for i in range(n)]

    for u,v in edges:
        adj_mat[u][v]=1
        adj_mat[v][u]=1
    return adj_mat

# implementing bfs
from collections import deque
def bfs(adj_mat,start):
    n = len(adj_mat)
    visited = [False]*n
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            print(node,end=" ")
            visited[node]= True
            for neighbor in range(n):
                if adj_mat[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)


adj_mat = create_mat(3,[[0,1],[1,1],[2,2],[1,2]])

print("Adjacency matrix")

for row in adj_mat:
    print(row)

print("BFS")

bfs(adj_mat,0)



