import networkx as nx

class GraphModel:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight=1):
        self.graph.add_edge(node1, node2, weight=weight)

    def number_of_vertices(self):
        return self.graph.number_of_nodes()

    def number_of_edges(self):
        return self.graph.number_of_edges()

    def get_number_of_vertices(self):
        return self.number_of_vertices()

    def get_number_of_edges(self):
        return self.number_of_edges()

    def get_graph_structure(self):
        return self.graph.edges()

    def analyze_graph(self):
        return {
            "vertices": self.number_of_vertices(),
            "edges": self.number_of_edges(),
            "structure": self.get_graph_structure()
        }