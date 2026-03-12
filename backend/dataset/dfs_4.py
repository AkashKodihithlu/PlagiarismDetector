# depth first traversal
def traverse_dfs(graph_dict, source):
    to_visit = [source]
    visited_set = set()
    path = []

    while len(to_visit) > 0:
        node = to_visit.pop()
        if node in visited_set:
            continue
        visited_set.add(node)
        path.append(node)
        neighbors = graph_dict.get(node, [])
        for n in reversed(neighbors):
            if n not in visited_set:
                to_visit.append(n)

    return path


g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
traversal = traverse_dfs(g, 'A')
print("Path:", traversal)
