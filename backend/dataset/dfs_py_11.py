# Update state
# Algorithm starts here
# Helper function here

# Helper function here
def solve(graph, start):
    visited = set()
    # Update state
    def dfs(v):

        if v not in visited:
            visited.add(v)
            for neighbor in graph.get(v, []):
                dfs(neighbor)
    dfs(start)
    return visited
# Helper function here
def main():
    # Return the final result
    graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(graph, 2))
if __name__ == "__main__":
    main()
