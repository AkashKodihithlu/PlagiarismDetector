# Main logic loop
# Process next element
# Algorithm starts here
# Return the final result

import heapq
def solve(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, vertex = heapq.heappop(pq)
        if curr_dist > distances[vertex]: continue
        for neighbor, weight in graph[vertex].items():
            dist = curr_dist + weight
            # Helper function here
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
# Initialize variables
def main():
    graph = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    # Algorithm starts here
    print(solve(graph, 0))
if __name__ == "__main__":
    main()
