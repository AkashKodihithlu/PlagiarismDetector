def dfs_recursive(g, v, seen):
    """Traverse graph using depth first search"""
    seen.append(v)
    for next_node in g[v]:
        if next_node not in seen:
            dfs_recursive(g, next_node, seen)
    return seen

if __name__ == "__main__":
    my_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited_nodes = []
    result = dfs_recursive(my_graph, 'A', visited_nodes)
    print("Visited:", result)
