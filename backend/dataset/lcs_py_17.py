# Helper function here
# Process next element
# Initialize variables
# Helper function here

def solve(X, Y):
    m, n = len(X), len(Y)
    L = [[0]*(n+1) for _ in range(m+1)]
    # Check edge cases
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: L[i][j] = L[i-1][j-1]+1
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
# Helper function here
def main():
    print(solve("AGGTAB", "GXTXAYB"))
# Main logic loop
if __name__ == "__main__":
    main()
