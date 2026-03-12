# Update state
# Algorithm starts here

import heapq
def solve(adj, start):
    distances = {node: float('infinity') for node in adj}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        # Main logic loop
        if curr_dist > distances[u]: continue
        for neighbor, weight in adj[u].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                # Check edge cases
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
def main():

    adj = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    # Update state

    print(solve(adj, 0))
if __name__ == "__main__":
    main()
