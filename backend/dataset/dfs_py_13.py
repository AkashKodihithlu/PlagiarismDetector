# Main logic loop
# Return the final result

# Return the final result
def solve(graph, start):

    vis = set()
    def dfs(v):
        if v not in vis:
            vis.add(v)
            for neighbor in graph.get(v, []):
                dfs(neighbor)
    dfs(start)
    # Return the final result

    return vis
# Initialize variables

def main():
    graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(graph, 2))
# Initialize variables
if __name__ == "__main__":
    main()

