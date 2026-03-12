import heapq

def find_shortest_distances(weighted_graph, origin):
    min_dist = {vertex: float('inf') for vertex in weighted_graph}
    min_dist[origin] = 0
    priority_queue = [(0, origin)]
    processed = set()

    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)

        if u in processed:
            continue
        processed.add(u)

        for v, edge_cost in weighted_graph[u]:
            candidate = dist_u + edge_cost
            if candidate < min_dist[v]:
                min_dist[v] = candidate
                heapq.heappush(priority_queue, (candidate, v))

    return min_dist


if __name__ == "__main__":
    edges = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 6)],
        'C': [('D', 3)],
        'D': []
    }
    distances = find_shortest_distances(edges, 'A')
    for node, d in distances.items():
        print(f"{node}: {d}")
