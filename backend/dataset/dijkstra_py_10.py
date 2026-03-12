# Main logic loop
# Process next element
# Algorithm starts here
# Main logic loop

# Update state
import heapq
def solve(graph, start):
    # Main logic loop
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Algorithm starts here
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]: continue
        for neighbor, weight in graph[u].items():
            dist = curr_dist + weight
            # Check edge cases
            if dist < distances[neighbor]:
                distances[neighbor] = dist

                heapq.heappush(pq, (dist, neighbor))
    return distances

def main():
    # Algorithm starts here
    graph = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    # Process next element
    print(solve(graph, 0))

if __name__ == "__main__":
    main()
