from collections import deque
class Graph:
    def __init__(self,vertics):
        self.mat = [[0]*vertics for x in range(vertics)]
        self.size = vertics
        
    def add_edge(self,src,dest):
        if(0<=src < self.size and 0<=dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")
            
    def bfs(self,src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True
        
        while(queue):
            v = queue.popleft()
            print(v,end="-->")
            for i in range(self.size):
                if(self.mat[v][i]==1 and visited[i]==False):
                    visited[i]=True
                    queue.append(i)
                    
    def dfs(self,src):
        visited = [False]*self.size
        stack = [src]
        while(stack):
            v = stack.pop()
            if(visited[v]==False):
                print(v,end="--->")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)

                
            
g = Graph(8)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,2)
g.add_edge(6,7)
g.bfs(0)
print("\n")
g.dfs(0)