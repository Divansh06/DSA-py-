vertices = 3
adj_mat =[[0]*vertices for i in range(vertices)]

edges =[(0,1),(0,2)]

for u,v in edges:
    adj_mat[u][v]=1
    adj_mat[v][u]=1
for row in adj_mat:
    print(adj_mat)

for i in range(vertices):
    for j in range(vertices):
        if adj_mat[i][j]==1:
            print(f"{i} ---{j}")
