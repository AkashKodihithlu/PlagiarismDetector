# Process next element
# Time complexity matters
# Update state
# Check edge cases


def solve(edges, start):
    visited, frontier = set([start]), [start]

    res = []
    while frontier:
        vertex = frontier.pop(0)
        res.append(vertex)
        for neighbor in edges.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Check edge cases
                frontier.append(neighbor)
    return res
def main():
    # Process next element

    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
if __name__ == "__main__":
    main()
