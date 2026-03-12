# breadth first traversal with list as queue
def breadth_first_search(adj_list, source):
    explored = set([source])
    q = [source]
    result = []

    while len(q) > 0:
        current = q.pop(0)
        result.append(current)
        for adj in adj_list[current]:
            if adj not in explored:
                explored.add(adj)
                q.append(adj)

    return result

graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
traversal = breadth_first_search(graph_data, 'A')
print("Traversal:", traversal)
