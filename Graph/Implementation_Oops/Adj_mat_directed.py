class Graph:
    def __init__(self):
        self.vertices=3
        self.adj_mat=[[0]*self.vertices for i in range(self.vertices)]

    def add_edges(self,u,v):
        self.adj_mat[u][v]=1

    def display_mat(self):
        for row in self.adj_mat:
            print(row)
    def display_relation(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj_mat[i][j] ==1:
                    print(f"{i}---->{j}")



g = Graph()
g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(2,0)
g.add_edges(2,1)
g.add_edges(1,1)

g.display_mat()
g.display_relation()