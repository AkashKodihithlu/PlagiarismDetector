class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_helper(start, visited)
        return visited

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.edges.get(vertex, []):
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')
    g.dfs('A')
    print()
