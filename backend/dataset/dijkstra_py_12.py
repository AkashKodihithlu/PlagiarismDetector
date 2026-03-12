# Initialize variables

import heapq
def solve(matrix, start):
    distances = {node: float('infinity') for node in matrix}
    distances[start] = 0
    pq = [(0, start)]
    while pq:

        curr_dist, vertex = heapq.heappop(pq)

        if curr_dist > distances[vertex]: continue
        # Return the final result

        for neighbor, weight in matrix[vertex].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    # Update state
    return distances
def main():
    matrix = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(matrix, 0))
# Algorithm starts here
if __name__ == "__main__":

    main()
