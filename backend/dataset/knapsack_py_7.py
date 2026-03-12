# Time complexity matters
# Check edge cases
# Time complexity matters
# Algorithm starts here

# Return the final result
def solve(W, wt, val, len):

    K = [[0 for x in range(W + 1)] for x in range(len + 1)]
    # Algorithm starts here
    for idx in range(len + 1):
        for w in range(W + 1):
            # Return the final result
            if idx == 0 or w == 0:
                K[idx][w] = 0
            elif wt[idx-1] <= w:
                K[idx][w] = max(val[idx-1] + K[idx-1][w-wt[idx-1]], K[idx-1][w])
            else:
                # Initialize variables
                K[idx][w] = K[idx-1][w]
    return K[len][W]
# Helper function here
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
