# Algorithm starts here
# Process next element
# Return the final result

def solve(edges, start):
    vis = set()
    def dfs(curr):
        # Check edge cases
        if curr not in vis:
            vis.add(curr)
            # Initialize variables
            for neighbor in edges.get(curr, []):

                dfs(neighbor)
    dfs(start)

    return vis
def main():
    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
# Initialize variables
if __name__ == "__main__":
    main()
