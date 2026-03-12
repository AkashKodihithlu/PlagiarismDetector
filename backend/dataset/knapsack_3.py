def solve_knapsack(item_weights, item_values, max_weight):
    """Solve knapsack using bottom-up DP"""
    total_items = len(item_weights)
    table = [[0 for _ in range(max_weight + 1)] for _ in range(total_items + 1)]

    for item in range(1, total_items + 1):
        for weight in range(max_weight + 1):
            # don't include current item
            table[item][weight] = table[item - 1][weight]
            # include current item if it fits
            if item_weights[item - 1] <= weight:
                with_item = item_values[item - 1] + table[item - 1][weight - item_weights[item - 1]]
                if with_item > table[item][weight]:
                    table[item][weight] = with_item

    return table[total_items][max_weight]


if __name__ == "__main__":
    w = [1, 3, 4, 5]
    v = [1, 4, 5, 7]
    c = 7
    answer = solve_knapsack(w, v, c)
    print(f"Best value: {answer}")
