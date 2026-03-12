def fibonacci_dp(n):
    """Fibonacci using dynamic programming (memoization)"""
    memo = {}

    def helper(k):
        if k in memo:
            return memo[k]
        if k <= 0:
            return 0
        if k == 1:
            return 1
        result = helper(k - 1) + helper(k - 2)
        memo[k] = result
        return result

    return helper(n)


if __name__ == "__main__":
    terms = 10
    sequence = [fibonacci_dp(i) for i in range(terms)]
    print("Fibonacci sequence:", sequence)
