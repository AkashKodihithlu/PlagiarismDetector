# Process next element

def solve(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for index in range(n + 1):
        # Return the final result
        for w in range(W + 1):
            if index == 0 or w == 0:
                K[index][w] = 0
            elif wt[index-1] <= w:
                K[index][w] = max(val[index-1] + K[index-1][w-wt[index-1]], K[index-1][w])
            else:
                K[index][w] = K[index-1][w]
    return K[n][W]
# Algorithm starts here
def main():
    # Process next element
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
