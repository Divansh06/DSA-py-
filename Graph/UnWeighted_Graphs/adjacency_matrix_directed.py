vertices = 3

adj_mat=[[0]*3 for i in range(vertices)]

edge =[(1,2,2),(2,1,3),(0,2,1)]

for u,v,w in edge:
    adj_mat[u][v]=1

# for row in adj_mat:
#     print(row)

for i in range(vertices):
    for j in range(vertices):

        if adj_mat[i][j]==1:
            print(f"{i} -----> {j}")

