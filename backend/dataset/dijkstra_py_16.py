# Algorithm starts here
# Time complexity matters
# Process next element

import heapq
def solve(graph, start):
    # Update state
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distances[node]: continue

        for neighbor, weight in graph[node].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                # Check edge cases
                heapq.heappush(pq, (dist, neighbor))
    return distances
# Return the final result
def main():
    graph = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(graph, 0))
if __name__ == "__main__":
    main()
