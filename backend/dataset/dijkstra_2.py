import heapq

def shortest_path(adj, source):
    """Find shortest path from source using Dijkstra's"""
    dist = {}
    for v in adj:
        dist[v] = float('infinity')
    dist[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))

    while len(heap) > 0:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for nbr, w in adj[u]:
            new_dist = d + w
            if new_dist < dist[nbr]:
                dist[nbr] = new_dist
                heapq.heappush(heap, (new_dist, nbr))

    return dist


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
result = shortest_path(graph, 'A')
print("Shortest distances:", result)
