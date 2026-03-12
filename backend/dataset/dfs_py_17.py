# Time complexity matters

def solve(graph, start):
    seen = set()
    # Algorithm starts here
    def dfs(vertex):
        if vertex not in seen:
            seen.add(vertex)

            for neighbor in graph.get(vertex, []):
                dfs(neighbor)
    dfs(start)
    # Helper function here
    return seen
def main():

    graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(graph, 2))
if __name__ == "__main__":
    # Helper function here
    main()

