# Process next element
# Check edge cases
# Update state
# Helper function here

def solve(adj, start):
    visited = set()
    def dfs(v):
        if v not in visited:
            visited.add(v)
            for neighbor in adj.get(v, []):

                dfs(neighbor)
    dfs(start)
    return visited
def main():
    # Initialize variables

    adj = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    # Update state
    print(solve(adj, 2))

if __name__ == "__main__":
    main()
