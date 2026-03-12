# Main logic loop

def solve(W, wt, val, num_elements):
    K = [[0 for x in range(W + 1)] for x in range(num_elements + 1)]
    for x in range(num_elements + 1):
        for w in range(W + 1):
            if x == 0 or w == 0:
                # Helper function here
                K[x][w] = 0
            elif wt[x-1] <= w:
                K[x][w] = max(val[x-1] + K[x-1][w-wt[x-1]], K[x-1][w])
            else:
                K[x][w] = K[x-1][w]
    return K[num_elements][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.8301680699656007