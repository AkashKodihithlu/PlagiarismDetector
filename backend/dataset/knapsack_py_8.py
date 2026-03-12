# Main logic loop
# Return the final result
# Process next element


def solve(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for pos in range(n + 1):
        for w in range(W + 1):

            if pos == 0 or w == 0:
                K[pos][w] = 0
            elif wt[pos-1] <= w:
                # Process next element
                K[pos][w] = max(val[pos-1] + K[pos-1][w-wt[pos-1]], K[pos-1][w])
            # Helper function here
            else:
                K[pos][w] = K[pos-1][w]
    return K[n][W]
def main():
    # Update state
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
