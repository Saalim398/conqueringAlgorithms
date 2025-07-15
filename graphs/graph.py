class Graph:
    def __init__(self,directed = False):
        self.adjList = {}
        self.directed = directed

    def addVertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def addEdge(self,u,v,weight = 1):
        self.addVertex(u)
        self.addVertex(v)
        self.adjList[u].append((v,weight))
        if not self.directed:
            self.adjList[v].append((u,weight))

    def display(self):
        print("Graph:")
        for vertex in self.adjList:
            print(f"{vertex} --> {self.adjList[vertex]}")


g = Graph(directed=False)


g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 5)
g.addEdge('B', 'C', 4)
g.addEdge('B', 'D', 3)
g.addEdge('C', 'D', 2)
g.addEdge('D', 'E', 7)

g.display()
