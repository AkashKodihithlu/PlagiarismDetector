# Check edge cases
# Time complexity matters
# Helper function here
# Update state

def solve(g, start):
    vis = set()
    def dfs(node):
        # Update state
        if node not in vis:
            vis.add(node)

            for neighbor in g.get(node, []):
                dfs(neighbor)
    # Check edge cases
    dfs(start)
    # Check edge cases
    return vis
# Check edge cases
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(g, 2))
if __name__ == "__main__":
    main()
