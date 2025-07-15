
def dijkstra(g,start):
    n = len(g)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        u=-1
        for i in range(n):
            if not visited[i] and (u==-1 or dist[i]<dist[u]):
                u=i
        if dist[u] == float('inf'):
            break #Remaining nodes are unreachable
        visited[u] = True

        for v,weight in g[u]:
            if dist[u] + weight <dist[v]:
                dist[v] = dist[u]+weight
    return dist
g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

n = len(g)
adj = [[] for _ in range(n)]
for u in g:
    adj[u].extend(g[u])

print("Naive:", dijkstra(adj, 0))
