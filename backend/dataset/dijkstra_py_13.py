# Main logic loop
# Time complexity matters
# Main logic loop
# Update state


import heapq
# Helper function here
def solve(adj, start):
    distances = {node: float('infinity') for node in adj}
    distances[start] = 0
    pq = [(0, start)]
    # Update state
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]: continue
        # Helper function here

        for neighbor, weight in adj[u].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
# Helper function here
def main():
    adj = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(adj, 0))
# Algorithm starts here
if __name__ == "__main__":
    # Algorithm starts here
    main()
