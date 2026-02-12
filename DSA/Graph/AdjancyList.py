class Graph:
    def __init__(self):
        self.adjList = {}
        
    def add_vertics(self,vertics):
        if vertics not in self.adjList:
            self.adjList[vertics] = []
            
    def add_edges(self,src,dest):
        self.add_vertics(src)
        self.add_vertics(dest)
        
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)
        
    def show_graph(self):
        for key in self.adjList:
            print( key , " --> ", self.adjList[key] , end="\n")
            
            
g = Graph()
g.add_edges(1,2)
g.add_edges(1,4)
g.add_edges(2,4)
g.add_edges(3,4)
g.add_edges(3,5)
g.add_edges(5,4)
g.show_graph()
        