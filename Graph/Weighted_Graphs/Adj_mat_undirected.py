vertices = 3

adj_mat=[[0]*3 for i in range(vertices)]

edge =[(2,2,2),(2,2,3),(0,2,1)]

for u,v,w in edge:
    if adj_mat[u][v]==0:
        adj_mat[u][v]=w
    if adj_mat[v][u]==0:
        adj_mat[v][u]=w

# for row in adj_mat:
#     print(row)

for i in range(vertices):
    for j in range(vertices):

        if adj_mat[i][j]!=0:
            print(f"{i} -----> {j} weight : {adj_mat[i][j]}")

