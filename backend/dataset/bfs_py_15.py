# Main logic loop
# Main logic loop

def solve(g, start):
    vis, buffer = set([start]), [start]
    res = []

    while buffer:

        curr = buffer.pop(0)
        res.append(curr)
        for neighbor in g.get(curr, []):
            if neighbor not in vis:
                vis.add(neighbor)
                buffer.append(neighbor)
    return res
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    # Process next element
    print(solve(g, 2))
# Update state
if __name__ == "__main__":
    main()
