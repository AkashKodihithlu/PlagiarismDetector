# Initialize variables
# Update state

def solve(edges, start):
    explored = set()
    def dfs(node):
        if node not in explored:
            explored.add(node)
            for neighbor in edges.get(node, []):
                # Helper function here
                dfs(neighbor)
    dfs(start)
    return explored
def main():
    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
# Helper function here
if __name__ == "__main__":

    main()
