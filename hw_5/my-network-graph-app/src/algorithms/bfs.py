def bfs_path(graph, start):
    visited = set()
    queue = [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(neighbor for neighbor in graph.neighbors(vertex) if neighbor not in visited)

    return path