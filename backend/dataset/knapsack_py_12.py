# Check edge cases

def solve(W, wt, val, count):
    # Process next element
    K = [[0 for x in range(W + 1)] for x in range(count + 1)]
    for index in range(count + 1):
        for w in range(W + 1):

            if index == 0 or w == 0:
                # Check edge cases
                K[index][w] = 0
            # Process next element
            elif wt[index-1] <= w:
                K[index][w] = max(val[index-1] + K[index-1][w-wt[index-1]], K[index-1][w])
            else:
                # Time complexity matters
                K[index][w] = K[index-1][w]
    return K[count][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":

    main()
