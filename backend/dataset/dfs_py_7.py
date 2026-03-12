# Update state
# Helper function here
# Return the final result
# Main logic loop

def solve(g, start):

    explored = set()
    def dfs(vertex):
        if vertex not in explored:
            explored.add(vertex)
            for neighbor in g.get(vertex, []):
                # Process next element
                dfs(neighbor)
    dfs(start)
    return explored
def main():
    # Return the final result
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    # Helper function here
    print(solve(g, 2))
if __name__ == "__main__":
    main()
