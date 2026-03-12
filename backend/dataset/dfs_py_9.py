# Update state
# Initialize variables

def solve(g, start):
    vis = set()
    def dfs(node):
        if node not in vis:
            vis.add(node)
            # Check edge cases
            for neighbor in g.get(node, []):
                dfs(neighbor)
    dfs(start)

    return vis
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(g, 2))
# Initialize variables
if __name__ == "__main__":

    main()
