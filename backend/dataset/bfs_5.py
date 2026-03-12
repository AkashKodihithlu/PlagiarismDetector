from collections import deque

def run_bfs(edges, begin):
    visited_nodes = set()
    visited_nodes.add(begin)
    processing_queue = deque()
    processing_queue.append(begin)
    output = []

    while len(processing_queue) > 0:
        item = processing_queue.popleft()
        output.append(item)
        neighbors = edges.get(item, [])
        for nb in neighbors:
            if nb not in visited_nodes:
                visited_nodes.add(nb)
                processing_queue.append(nb)

    return output


edges = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("Result:", run_bfs(edges, 'A'))
