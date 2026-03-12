# space optimized LCS using two rows
def lcs_space_optimized(x, y):
    m = len(x)
    n = len(y)

    # only keep two rows
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]

    return prev[n]


if __name__ == "__main__":
    first = "ABCBDAB"
    second = "BDCAB"
    res = lcs_space_optimized(first, second)
    print("LCS length:", res)
