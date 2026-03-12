import heapq

class DijkstraSolver:
    def __init__(self, graph_dict):
        self.graph = graph_dict

    def compute(self, start):
        dist_map = {}
        for key in self.graph:
            dist_map[key] = float('inf')
        dist_map[start] = 0
        pq = [(0, start)]

        while pq:
            curr_d, curr_v = heapq.heappop(pq)
            if curr_d > dist_map[curr_v]:
                continue
            for adj_v, adj_w in self.graph.get(curr_v, []):
                new_d = curr_d + adj_w
                if new_d < dist_map[adj_v]:
                    dist_map[adj_v] = new_d
                    heapq.heappush(pq, (new_d, adj_v))

        return dist_map


g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
solver = DijkstraSolver(g)
print("Result:", solver.compute('A'))
