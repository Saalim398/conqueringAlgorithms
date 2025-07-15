# procedual way to write prims Algorithm
def primsAlgo(graph , start):
    visited = set()
    mstEdges = []
    totalCost = 0

    visited.add(start)

    while len(visited) < len(graph):
        minEdge = None
        minWeight = float('inf')

        for u in visited:
            for v,weight in graph[u]:
                if v not in visited and weight < minWeight:
                    minEdge = (u,v,weight)
                    minWeight = weight
        
        if minEdge is None:
            break

        u,v,weight = minEdge
        visited.add(v)
        mstEdges.append((u,v,weight))
        totalCost+=weight
    return mstEdges,totalCost

graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 4), ('D', 3)],
    'C': [('A', 5), ('B', 4), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 7)],
    'E': [('D', 7)]
}

mst, cost = primsAlgo(graph, 'A')

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total cost of MST:", cost)
