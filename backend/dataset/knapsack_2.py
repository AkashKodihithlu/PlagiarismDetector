# knapsack recursive with memoization
def knapsack_memo(wt, val, W, n, memo=None):
    if memo is None:
        memo = {}
    if (n, W) in memo:
        return memo[(n, W)]
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        result = knapsack_memo(wt, val, W, n - 1, memo)
    else:
        include = val[n - 1] + knapsack_memo(wt, val, W - wt[n - 1], n - 1, memo)
        exclude = knapsack_memo(wt, val, W, n - 1, memo)
        result = max(include, exclude)
    memo[(n, W)] = result
    return result

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
num_items = len(weights)
print("Maximum value:", knapsack_memo(weights, values, capacity, num_items))
