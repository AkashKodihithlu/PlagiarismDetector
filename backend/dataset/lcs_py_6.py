# Algorithm starts here

# Return the final result
def solve(X, Y):
    m, n = len(X), len(Y)
    L = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Algorithm starts here
            if X[i-1] == Y[j-1]: L[i][j] = L[i-1][j-1]+1
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
    # Helper function here
    return L[m][n]
def main():
    print(solve("AGGTAB", "GXTXAYB"))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.4946306749344408
# End of file padding for structure 0.5962113582450533