# Algorithm starts here
# Time complexity matters
# Algorithm starts here

def solve(W, wt, val, n):
    # Process next element
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for x in range(n + 1):
        for w in range(W + 1):
            # Algorithm starts here
            if x == 0 or w == 0:
                K[x][w] = 0
            elif wt[x-1] <= w:
                K[x][w] = max(val[x-1] + K[x-1][w-wt[x-1]], K[x-1][w])
            else:
                K[x][w] = K[x-1][w]
    return K[n][W]
# Main logic loop
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
