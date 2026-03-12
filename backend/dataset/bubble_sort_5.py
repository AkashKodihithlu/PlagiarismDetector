def do_bubble_sort(values):
    total = len(values)
    for a in range(total - 1):
        for b in range(total - 1 - a):
            # swap if current element is greater
            if values[b] > values[b + 1]:
                values[b], values[b + 1] = values[b + 1], values[b]
    return values


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = do_bubble_sort(arr)
print(sorted_arr)
