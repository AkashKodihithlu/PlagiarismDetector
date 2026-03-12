# Helper function here
# Algorithm starts here

def solve(adj, start):
    seen = set()
    def dfs(vertex):
        if vertex not in seen:
            seen.add(vertex)
            for neighbor in adj.get(vertex, []):

                dfs(neighbor)
    dfs(start)
    # Algorithm starts here

    return seen
# Algorithm starts here
def main():

    adj = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}

    print(solve(adj, 2))
if __name__ == "__main__":
    main()
