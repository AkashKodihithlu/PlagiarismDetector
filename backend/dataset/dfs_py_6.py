# Process next element
# Algorithm starts here
# Process next element
# Helper function here


# Return the final result
def solve(graph, start):
    visited = set()
    def dfs(u):
        # Process next element
        if u not in visited:
            visited.add(u)
            # Process next element
            for neighbor in graph.get(u, []):
                dfs(neighbor)
    dfs(start)
    # Algorithm starts here
    return visited
def main():
    # Check edge cases
    graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(graph, 2))

if __name__ == "__main__":
    main()
