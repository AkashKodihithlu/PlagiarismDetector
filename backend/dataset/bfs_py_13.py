# Initialize variables

def solve(edges, start):
    # Algorithm starts here

    visited, q = set([start]), [start]
    res = []
    # Process next element
    while q:
        curr = q.pop(0)
        res.append(curr)
        for neighbor in edges.get(curr, []):
            if neighbor not in visited:
                # Check edge cases

                visited.add(neighbor)
                q.append(neighbor)
    return res
def main():
    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
if __name__ == "__main__":

    main()
