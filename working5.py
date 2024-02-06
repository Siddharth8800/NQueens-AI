import numpy as np
import queue

vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))
graph = np.zeros((vertices, vertices), dtype=int)
heuristic_values = np.zeros(vertices, dtype=int)

def add_edge(source, destination, weight = 1):
    graph[source][destination] = weight
    graph[destination][source] = weight

def assign_heuristic_value(node, value):
    heuristic_values[node] = value

for _ in range(edges):
    i, j, w= map(int, input("Enter the vertices of an edge and its weight separated by space: ").split())
    add_edge(i, j, w)

for node in range(vertices):
    value = int(input(f"Enter the heuristic value for node {node}: "))
    assign_heuristic_value(node, value)

start_node = int(input("Enter the starting node: "))
goal_node = int(input("Enter the goal node: "))

def a_star_search(graph, heuristic_values, start_node, goal_node):
    open_nodes = queue.PriorityQueue()
    open_nodes.put((0, start_node))
    closed_nodes = set()
    while not open_nodes.empty():
        current_cost, current_node = open_nodes.get()
        closed_nodes.add(current_node)
        print("Open Nodes:", open_nodes.queue)
        print("Closed Nodes:", closed_nodes)
        if current_node == goal_node:
            print("Goal reached")
            return
        for neighbor in range(vertices):
            if graph[current_node][neighbor] != 0 and neighbor not in closed_nodes:
                neighbor_cost = current_cost + graph[current_node][neighbor] + heuristic_values[neighbor]
                open_nodes.put((neighbor_cost, neighbor))

a_star_search(graph, heuristic_values, start_node, goal_node)
