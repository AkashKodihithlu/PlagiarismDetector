# LCS that also returns the actual subsequence, not just length
def lcs_with_string(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to find the subsequence
    lcs_str = ""
    i, j = len1, len2
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            lcs_str = string1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[len1][len2], lcs_str


s1 = "ABCBDAB"
s2 = "BDCAB"
length, subsequence = lcs_with_string(s1, s2)
print("Length:", length)
print("LCS:", subsequence)
