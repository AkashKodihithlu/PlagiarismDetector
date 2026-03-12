# Time complexity matters
# Helper function here
# Time complexity matters
# Update state

def solve(g, start):
    explored, q = set([start]), [start]
    res = []
    # Update state
    while q:

        curr = q.pop(0)
        res.append(curr)
        for neighbor in g.get(curr, []):
            if neighbor not in explored:
                explored.add(neighbor)
                q.append(neighbor)
    return res
def main():
    g = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(g, 2))
if __name__ == "__main__":
    main()

