# My Network Graph Application

This project implements a graph using the NetworkX library to model a real-world network. It includes functionalities for visualizing the graph, analyzing its characteristics, and implementing various pathfinding algorithms.

## Project Structure

```
my-network-graph-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── graph_model.py         # Defines the GraphModel class
│   ├── visualization.py        # Functions for visualizing the graph
│   └── algorithms
│       ├── dfs.py             # Implements Depth-First Search (DFS)
│       ├── bfs.py             # Implements Breadth-First Search (BFS)
│       └── dijkstra.py         # Implements Dijkstra's algorithm
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Graph Model

The `GraphModel` class in `graph_model.py` utilizes the NetworkX library to create and manage the graph. It provides methods to add nodes and edges, analyze graph characteristics such as the number of vertices and edges, and retrieve the graph structure.

## Visualization

The `visualization.py` file contains functions that utilize Matplotlib to visualize the graph. It includes a function to display the graph and highlight specific paths found by the pathfinding algorithms.

## Pathfinding Algorithms

### Depth-First Search (DFS)

The DFS algorithm is implemented in `dfs.py`. The `dfs_path` function takes a graph and a starting node, returning a path found using the DFS approach.

### Breadth-First Search (BFS)

The BFS algorithm is implemented in `bfs.py`. The `bfs_path` function takes a graph and a starting node, returning a path found using the BFS approach.

### Dijkstra's Algorithm

Dijkstra's algorithm is implemented in `dijkstra.py`. The `dijkstra_shortest_path` function takes a graph and a starting node, returning the shortest path to all other nodes in a weighted graph.

## Analysis and Findings

The project includes an analysis of the characteristics of the graph, comparing the results of DFS and BFS in terms of pathfinding efficiency. Additionally, findings from Dijkstra's algorithm provide insights into the shortest paths within the graph.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

This will initialize the graph model, visualize the graph, and execute the pathfinding algorithms.