# space optimized knapsack using 1D array
def knapsack_optimized(wt, val, cap):
    n = len(wt)
    dp = [0] * (cap + 1)

    for i in range(n):
        j = cap
        while j >= wt[i]:
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
            j -= 1

    return dp[cap]


w_list = [1, 3, 4, 5]
v_list = [1, 4, 5, 7]
max_cap = 7
print("Optimal:", knapsack_optimized(w_list, v_list, max_cap))
