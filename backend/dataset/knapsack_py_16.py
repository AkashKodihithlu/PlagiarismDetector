# Update state
# Check edge cases


def solve(W, wt, val, size):
    # Initialize variables
    K = [[0 for x in range(W + 1)] for x in range(size + 1)]
    for index in range(size + 1):
        for w in range(W + 1):
            if index == 0 or w == 0:
                K[index][w] = 0
            # Initialize variables
            elif wt[index-1] <= w:
                K[index][w] = max(val[index-1] + K[index-1][w-wt[index-1]], K[index-1][w])
            else:
                # Initialize variables
                K[index][w] = K[index-1][w]
    return K[size][W]

def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
