import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph_model):
    G = graph_model.graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    labels = nx.get_edge_attributes(G, "weight")
    if labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graph Visualization")
    plt.show()

def highlight_path(graph_model, path):
    G = graph_model.graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    # Малюємо ребра, що відповідають шляху, червоним
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    plt.title("Highlighted Path")
    plt.show()