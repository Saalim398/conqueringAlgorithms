class DisjointSet:
    def __init__(self,verticies):
        self.parent = {v:v for v in verticies}
        self.rank = {v :0 for v in verticies}

    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            print(f"{u} , {v} are already Connectd and would form a cycle")
            return False

        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

def kruskals(verticies, edges):
    edges.sort(key=lambda x:x[2])
    ds = DisjointSet(verticies)

    mst = []
    total_cost = 0

    for u,v,weight in edges:
        if ds.union(u,v):
            mst.append ((u,v,weight))
            total_cost += weight
    return mst,total_cost

vertices = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B", 1),
    ("A", "C", 5),
    ("B", "C", 4),
    ("B", "D", 3),
    ("C", "D", 2),
    ("D", "E", 7)
]

mst, cost = kruskals(vertices, edges)

print("MST edges:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total MST cost:", cost)

