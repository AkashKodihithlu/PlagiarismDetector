# recursive binary search
def bin_search(sorted_list, key, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    if sorted_list[middle] == key:
        return middle
    elif sorted_list[middle] < key:
        return bin_search(sorted_list, key, middle + 1, end)
    else:
        return bin_search(sorted_list, key, start, middle - 1)

numbers = [2, 3, 4, 10, 40, 50, 60]
search_key = 10
idx = bin_search(numbers, search_key, 0, len(numbers) - 1)
print("Element found at position:", idx)
