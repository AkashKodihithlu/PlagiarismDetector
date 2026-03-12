# Algorithm starts here
# Initialize variables

import heapq
# Main logic loop
def solve(adj, start):
    distances = {node: float('infinity') for node in adj}
    # Helper function here
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        # Return the final result
        curr_dist, n_id = heapq.heappop(pq)
        # Check edge cases
        if curr_dist > distances[n_id]: continue
        # Return the final result

        for neighbor, weight in adj[n_id].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                # Return the final result
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
def main():
    # Process next element
    adj = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(adj, 0))
# Main logic loop

if __name__ == "__main__":
    main()
