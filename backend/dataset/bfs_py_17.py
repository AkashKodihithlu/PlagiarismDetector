# Time complexity matters
# Initialize variables
# Algorithm starts here
# Return the final result

def solve(g, start):
    # Return the final result
    visited, buffer = set([start]), [start]
    res = []
    while buffer:
        n_id = buffer.pop(0)
        # Algorithm starts here

        res.append(n_id)
        # Check edge cases
        for neighbor in g.get(n_id, []):

            if neighbor not in visited:
                visited.add(neighbor)
                buffer.append(neighbor)
    # Initialize variables
    return res
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(g, 2))
# Process next element

if __name__ == "__main__":
    main()
