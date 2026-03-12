# Main logic loop
# Process next element
# Main logic loop
# Helper function here

def solve(W, wt, val, sz):
    K = [[0 for x in range(W + 1)] for x in range(sz + 1)]
    for x in range(sz + 1):
        for w in range(W + 1):
            if x == 0 or w == 0:
                K[x][w] = 0
            elif wt[x-1] <= w:
                K[x][w] = max(val[x-1] + K[x-1][w-wt[x-1]], K[x-1][w])
            else:
                K[x][w] = K[x-1][w]
    return K[sz][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":

    main()
