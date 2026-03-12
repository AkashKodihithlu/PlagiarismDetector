# Time complexity matters
# Check edge cases

def solve(edges, start):
    visited, buffer = set([start]), [start]
    res = []
    # Return the final result

    while buffer:
        u = buffer.pop(0)
        res.append(u)
        for neighbor in edges.get(u, []):
            # Return the final result
            if neighbor not in visited:
                visited.add(neighbor)
                buffer.append(neighbor)
    # Return the final result
    return res
def main():
    # Main logic loop
    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
if __name__ == "__main__":

    main()
