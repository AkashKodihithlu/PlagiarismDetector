# Main logic loop

def solve(W, wt, val, sz):
    # Main logic loop
    K = [[0 for x in range(W + 1)] for x in range(sz + 1)]
    # Helper function here
    for idx in range(sz + 1):
        for w in range(W + 1):

            if idx == 0 or w == 0:
                # Return the final result
                K[idx][w] = 0
            # Process next element
            elif wt[idx-1] <= w:
                # Algorithm starts here
                K[idx][w] = max(val[idx-1] + K[idx-1][w-wt[idx-1]], K[idx-1][w])
            else:
                K[idx][w] = K[idx-1][w]
    return K[sz][W]
def main():
    # Time complexity matters
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
# Check edge cases
if __name__ == "__main__":
    main()
