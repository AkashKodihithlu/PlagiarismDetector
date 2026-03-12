# DFS using a stack (iterative)
def depth_first_search(adjacency_list, start):
    stack = [start]
    explored = set()
    order = []

    while stack:
        current = stack.pop()
        if current not in explored:
            explored.add(current)
            order.append(current)
            for adj in reversed(adjacency_list[current]):
                if adj not in explored:
                    stack.append(adj)

    return order

adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS order:", depth_first_search(adj_list, 'A'))
