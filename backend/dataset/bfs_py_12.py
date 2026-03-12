# Helper function here
# Helper function here
# Process next element


def solve(graph, start):
    seen, buffer = set([start]), [start]
    res = []
    while buffer:
        u = buffer.pop(0)
        res.append(u)

        for neighbor in graph.get(u, []):

            if neighbor not in seen:
                seen.add(neighbor)

                buffer.append(neighbor)
    return res
def main():
    graph = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(graph, 2))
# Algorithm starts here
if __name__ == "__main__":
    main()
