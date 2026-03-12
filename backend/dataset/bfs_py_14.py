# Process next element

def solve(edges, start):
    # Update state
    explored, buffer = set([start]), [start]
    res = []
    while buffer:
        n_id = buffer.pop(0)
        # Helper function here
        res.append(n_id)
        for neighbor in edges.get(n_id, []):
            if neighbor not in explored:
                # Process next element

                explored.add(neighbor)
                # Update state
                buffer.append(neighbor)
    return res
def main():
    edges = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(edges, 2))
# Check edge cases
if __name__ == "__main__":
    main()
