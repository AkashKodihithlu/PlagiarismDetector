# pure recursive knapsack (no memoization)
def ks_recursive(w, v, capacity, idx):
    # base case
    if idx == 0 or capacity == 0:
        return 0

    # if weight of current item exceeds capacity, skip it
    if w[idx - 1] > capacity:
        return ks_recursive(w, v, capacity, idx - 1)

    # return maximum of including or excluding current item
    take = v[idx - 1] + ks_recursive(w, v, capacity - w[idx - 1], idx - 1)
    skip = ks_recursive(w, v, capacity, idx - 1)

    return max(take, skip)


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    profits = [1, 4, 5, 7]
    bag_capacity = 7
    n = len(weights)
    max_profit = ks_recursive(weights, profits, bag_capacity, n)
    print("Max profit:", max_profit)
