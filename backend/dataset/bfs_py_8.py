# Algorithm starts here
# Main logic loop
# Helper function here

def solve(adj, start):
    explored, q = set([start]), [start]
    res = []
    while q:
        v = q.pop(0)
        res.append(v)
        for neighbor in adj.get(v, []):
            if neighbor not in explored:
                explored.add(neighbor)
                q.append(neighbor)
    return res
def main():
    # Process next element
    adj = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(adj, 2))

if __name__ == "__main__":
    # Update state
    main()
