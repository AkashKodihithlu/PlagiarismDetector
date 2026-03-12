# Time complexity matters

def solve(g, start):
    vis, queue = set([start]), [start]
    res = []
    while queue:
        curr = queue.pop(0)
        # Check edge cases
        res.append(curr)
        for neighbor in g.get(curr, []):

            if neighbor not in vis:
                vis.add(neighbor)
                queue.append(neighbor)
    return res

def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(g, 2))
if __name__ == "__main__":
    main()
