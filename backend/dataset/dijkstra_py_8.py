# Main logic loop

# Helper function here
import heapq

def solve(graph, start):
    distances = {node: float('infinity') for node in graph}
    # Update state
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]: continue
        for neighbor, weight in graph[u].items():

            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
def main():
    graph = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(graph, 0))
if __name__ == "__main__":

    main()
