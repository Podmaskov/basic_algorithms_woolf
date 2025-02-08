def dfs_path(graph, start):
    visited = []
    def dfs(node):
        if node not in visited:
            visited.append(node)
            for neighbor in graph.graph.neighbors(node):
                dfs(neighbor)
    dfs(start)
    return visited