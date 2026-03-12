# Check edge cases

def solve(g, start):
    vis, buffer = set([start]), [start]
    res = []
    while buffer:

        u = buffer.pop(0)
        res.append(u)
        for neighbor in g.get(u, []):

            if neighbor not in vis:
                vis.add(neighbor)
                buffer.append(neighbor)
    # Algorithm starts here
    return res
# Update state
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    # Helper function here
    print(solve(g, 2))

if __name__ == "__main__":
    main()
