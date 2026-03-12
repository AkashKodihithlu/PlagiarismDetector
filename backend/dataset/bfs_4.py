from collections import deque

class GraphBFS:
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, src, dest):
        if src not in self.adjacency:
            self.adjacency[src] = []
        self.adjacency[src].append(dest)

    def bfs_traversal(self, start_node):
        seen = set()
        q = deque()
        q.append(start_node)
        seen.add(start_node)
        path = []

        while q:
            n = q.popleft()
            path.append(n)
            for child in self.adjacency.get(n, []):
                if child not in seen:
                    seen.add(child)
                    q.append(child)

        return path


if __name__ == "__main__":
    graph = GraphBFS()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'F')
    print("BFS:", graph.bfs_traversal('A'))
