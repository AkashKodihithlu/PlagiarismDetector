# dijkstra without heapq - naive implementation
def dijkstra_naive(graph, src):
    unvisited = set(graph.keys())
    cost = {node: float('inf') for node in graph}
    cost[src] = 0

    while unvisited:
        # find unvisited node with minimum cost
        current = None
        for node in unvisited:
            if current is None or cost[node] < cost[current]:
                current = node

        if cost[current] == float('inf'):
            break

        unvisited.remove(current)

        for neighbor, edge_weight in graph[current]:
            tentative = cost[current] + edge_weight
            if tentative < cost[neighbor]:
                cost[neighbor] = tentative

    return cost

if __name__ == "__main__":
    g = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 6)],
        'C': [('D', 3)],
        'D': []
    }
    print(dijkstra_naive(g, 'A'))
