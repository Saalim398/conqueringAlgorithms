g = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}



visited = []
queue = []

def bfs(visited, g, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for next in g[m]:
            if next not in visited:
                visited.append(next)
                queue.append(next)

print("The following is bfs: ")
bfs(visited, g, "5")
