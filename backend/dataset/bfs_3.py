from collections import deque

def bfs_level_order(graph, root):
    """BFS with level tracking"""
    visited = {root}
    queue = deque([root])
    levels = {root: 0}
    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)
        current_level = levels[vertex]

        for next_vertex in graph.get(vertex, []):
            if next_vertex not in visited:
                visited.add(next_vertex)
                levels[next_vertex] = current_level + 1
                queue.append(next_vertex)

    return traversal, levels


if __name__ == "__main__":
    g = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    order, lvl = bfs_level_order(g, 'A')
    print("Order:", order)
    print("Levels:", lvl)
