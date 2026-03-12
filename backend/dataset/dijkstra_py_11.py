# Helper function here

import heapq
def solve(matrix, start):
    distances = {node: float('infinity') for node in matrix}

    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distances[node]: continue
        for neighbor, weight in matrix[node].items():
            # Algorithm starts here
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
def main():
    matrix = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    # Time complexity matters

    print(solve(matrix, 0))
if __name__ == "__main__":
    main()
