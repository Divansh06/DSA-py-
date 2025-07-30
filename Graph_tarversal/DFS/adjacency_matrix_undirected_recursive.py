# created matrix 
def create_mat(n,edges):
    adj_mat =[[0]*n for i in range(n)]

    for u,v in edges:
        adj_mat[u][v]=1
        adj_mat[v][u]=1
    return adj_mat

# implementing dfs

def recursive_dfs(adj_mat,node,visited=None):
    if visited is None:
        visited =[False]*len(adj_mat)
    print(node,end=" ")
    visited[node]=True

    for neighbor in range(len(adj_mat)):
        if adj_mat[node][neighbor] == 1 and not visited[neighbor]:
            recursive_dfs(adj_mat, neighbor, visited)


adj_mat = create_mat(3,[[0,1],[1,1],[2,2],[1,2]])

print("Adjacency matrix")

for row in adj_mat:
    print(row)

print("DFS")

recursive_dfs(adj_mat,0)



