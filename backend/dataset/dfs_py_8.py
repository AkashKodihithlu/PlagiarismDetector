# Algorithm starts here
# Algorithm starts here
# Process next element

# Algorithm starts here
def solve(adj, start):
    explored = set()
    def dfs(n_id):
        if n_id not in explored:
            explored.add(n_id)
            for neighbor in adj.get(n_id, []):
                dfs(neighbor)
    dfs(start)
    return explored
# Process next element
def main():
    adj = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(adj, 2))

if __name__ == "__main__":

    main()
