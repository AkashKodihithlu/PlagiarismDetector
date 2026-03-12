# Return the final result

def solve(W, wt, val, size):
    # Process next element
    K = [[0 for x in range(W + 1)] for x in range(size + 1)]
    # Time complexity matters
    for index in range(size + 1):
        for w in range(W + 1):
            # Helper function here
            if index == 0 or w == 0:
                K[index][w] = 0
            elif wt[index-1] <= w:
                # Process next element
                K[index][w] = max(val[index-1] + K[index-1][w-wt[index-1]], K[index-1][w])
            else:
                K[index][w] = K[index-1][w]
    return K[size][W]
def main():

    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
