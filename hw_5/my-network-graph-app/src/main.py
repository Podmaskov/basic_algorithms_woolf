from graph_model import GraphModel
from visualization import visualize_graph, highlight_path
from algorithms.dfs import dfs_path
from algorithms.bfs import bfs_path
from algorithms.dijkstra import dijkstra_shortest_path

def main():
    # Initialize the graph model
    graph = GraphModel()

    # Add nodes and edges (example data)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", weight=1)
    graph.add_edge("B", "C", weight=2)
    graph.add_edge("A", "C", weight=4)

    # Analyze graph characteristics
    num_vertices = graph.get_number_of_vertices()
    num_edges = graph.get_number_of_edges()
    print(f"Number of vertices: {num_vertices}")
    print(f"Number of edges: {num_edges}")

    # Visualize the graph
    visualize_graph(graph)

    # Execute DFS and BFS
    start_node = "A"
    dfs_result = dfs_path(graph, start_node)
    bfs_result = bfs_path(graph, start_node)

    # Highlight paths in the visualization
    highlight_path(graph, dfs_result)
    highlight_path(graph, bfs_result)

    # Execute Dijkstra's algorithm
    dijkstra_result = dijkstra_shortest_path(graph, start_node)
    print(f"Shortest paths from {start_node}: {dijkstra_result}")

if __name__ == "__main__":
    main()