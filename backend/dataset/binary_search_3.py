def search_binary(array, value):
    """Performs binary search on a sorted array"""
    left = 0
    right = len(array) - 1

    while left <= right:
        center = left + (right - left) // 2

        if array[center] == value:
            return center
        elif array[center] < value:
            left = center + 1
        else:
            right = center - 1

    return -1


if __name__ == "__main__":
    test_arr = [2, 3, 4, 10, 40, 50, 60]
    target_val = 10
    pos = search_binary(test_arr, target_val)
    if pos != -1:
        print(f"Element {target_val} found at index {pos}")
    else:
        print("Element not found")
