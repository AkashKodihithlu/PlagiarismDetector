# recursive LCS with memoization
def longest_common_subseq(x, y, i, j, cache):
    if i == 0 or j == 0:
        return 0
    if (i, j) in cache:
        return cache[(i, j)]
    if x[i - 1] == y[j - 1]:
        result = 1 + longest_common_subseq(x, y, i - 1, j - 1, cache)
    else:
        opt1 = longest_common_subseq(x, y, i - 1, j, cache)
        opt2 = longest_common_subseq(x, y, i, j - 1, cache)
        result = max(opt1, opt2)
    cache[(i, j)] = result
    return result

text1 = "ABCBDAB"
text2 = "BDCAB"
memo = {}
length = longest_common_subseq(text1, text2, len(text1), len(text2), memo)
print("Length of LCS:", length)
