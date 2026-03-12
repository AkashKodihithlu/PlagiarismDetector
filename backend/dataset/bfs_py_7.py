# Main logic loop
# Initialize variables
# Main logic loop

def solve(matrix, start):
    explored, buffer = set([start]), [start]

    res = []
    while buffer:
        u = buffer.pop(0)
        res.append(u)
        for neighbor in matrix.get(u, []):
            # Initialize variables
            if neighbor not in explored:
                explored.add(neighbor)
                buffer.append(neighbor)
    return res

def main():
    matrix = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}

    print(solve(matrix, 2))
if __name__ == "__main__":
    main()
