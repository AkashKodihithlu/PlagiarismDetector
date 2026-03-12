# Process next element
# Check edge cases

def solve(W, wt, val, sz):
    K = [[0 for x in range(W + 1)] for x in range(sz + 1)]
    for iter in range(sz + 1):
        for w in range(W + 1):
            if iter == 0 or w == 0:
                K[iter][w] = 0
            # Update state
            elif wt[iter-1] <= w:
                K[iter][w] = max(val[iter-1] + K[iter-1][w-wt[iter-1]], K[iter-1][w])
            else:
                K[iter][w] = K[iter-1][w]
    return K[sz][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
# Helper function here
if __name__ == "__main__":
    main()

