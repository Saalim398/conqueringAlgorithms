import heapq

class PrimMST:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self, start):
        visited = set()
        min_heap = []
        mst_edges = []
        total_cost = 0

        visited.add(start)

        
        for neighbor, weight in self.graph[start]:
            heapq.heappush(min_heap, (weight, start, neighbor))

        while min_heap and len(visited) < len(self.graph):
            weight, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            mst_edges.append((u, v, weight))
            total_cost += weight

            for neighbor, w in self.graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, v, neighbor))

        return mst_edges, total_cost


graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 4), ('D', 3)],
    'C': [('A', 5), ('B', 4), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 7)],
    'E': [('D', 7)]
}


prim = PrimMST(graph)


mst, cost = prim.find_mst('A')


print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total cost of MST:", cost)
