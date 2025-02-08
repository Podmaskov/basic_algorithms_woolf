def dijkstra_shortest_path(graph, start_node):
    import networkx as nx

    # Initialize the distance for each node
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0

    # Create a priority queue to hold nodes to explore
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can only be added once to the priority queue
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances