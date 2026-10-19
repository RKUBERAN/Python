def bfs(graph, start, goal):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for child in graph[node]:
                queue.append(path + [child])

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [],
    'G': ['I'], 'I': []
}

print(bfs(graph, 'A', 'I'))
