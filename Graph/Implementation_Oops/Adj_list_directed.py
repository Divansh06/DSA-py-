# directed graph
class graph:
    def __init__(self):
        self.graph ={}
        
    def add_edges(self,source,destination):
        if source not in self.graph:
            self.graph[source] =[]
        self.graph[source].append(destination)
    
    def display(self):
        for node in self.graph:
            print(f"{node} --->{self.graph[node]}")
            
g = graph()
g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(2,3)
g.add_edges(2,1)
g.add_edges(3,4)
g.add_edges(4,5)
g.display()