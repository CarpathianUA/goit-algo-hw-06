import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

from bfs import bfs_recursive
from dfs import dfs_recursive
from dijkstra import dijkstra

from constants import san_francisco_transport_map


# task 1
san_francisco_transport_graph = nx.Graph()

for node, neighbors in san_francisco_transport_map.items():
    for neighbor, weight in neighbors.items():
        san_francisco_transport_graph.add_edge(node, neighbor, weight=weight)


print("Num of nodes:", san_francisco_transport_graph.number_of_nodes())
print("Num of edges:", san_francisco_transport_graph.number_of_edges())
print("List of nodes:", list(san_francisco_transport_graph.nodes()))
print("List of edges:", list(san_francisco_transport_graph.edges()))
print("Nodes degree:", dict(san_francisco_transport_graph.degree()))

pos = nx.shell_layout(san_francisco_transport_graph)
nx.draw(
    san_francisco_transport_graph,
    pos,
    with_labels=True,
    node_color="bisque",
)

edge_weights = nx.get_edge_attributes(san_francisco_transport_graph, "weight")
nx.draw_networkx_edge_labels(
    san_francisco_transport_graph, pos, edge_labels=edge_weights
)


start_node = "Palace_of_Fine_Arts"

# task 2
print("DFS:")
dfs_recursive(san_francisco_transport_graph, start_node)

print("\nBFS:")
bfs_recursive(san_francisco_transport_graph, deque([start_node]))

# task 3
print("\nDijkstra:")
print(dijkstra(san_francisco_transport_map, start_node))

plt.show()
