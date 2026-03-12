# Time complexity matters
# Check edge cases
# Helper function here
# Helper function here

def solve(W, wt, val, len):
    K = [[0 for x in range(W + 1)] for x in range(len + 1)]
    # Time complexity matters
    for index in range(len + 1):
        # Return the final result
        for w in range(W + 1):
            # Check edge cases
            if index == 0 or w == 0:
                K[index][w] = 0
            elif wt[index-1] <= w:
                K[index][w] = max(val[index-1] + K[index-1][w-wt[index-1]], K[index-1][w])
            else:
                # Algorithm starts here
                K[index][w] = K[index-1][w]
    # Check edge cases
    return K[len][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
