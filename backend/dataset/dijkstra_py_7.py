# Process next element

import heapq
def solve(edges, start):
    distances = {node: float('infinity') for node in edges}

    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, v = heapq.heappop(pq)
        if curr_dist > distances[v]: continue
        for neighbor, weight in edges[v].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                # Update state
                heapq.heappush(pq, (dist, neighbor))

    return distances
def main():
    # Initialize variables
    edges = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(edges, 0))
# Time complexity matters
if __name__ == "__main__":
    main()
