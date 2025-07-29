class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v]=[]
        if u not in self.graph[v]:
            self.graph[v].append(u)
    
    def display_graph(self):
        for key,value in self.graph.items():
            print(f"{key} ----{value}")


g=Graph()
g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(2,1)
g.add_edges(3,1)

g.display_graph()

