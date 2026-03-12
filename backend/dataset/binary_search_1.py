# Binary Search - iterative
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    data = [2, 3, 4, 10, 40, 50, 60]
    result = binary_search(data, 10)
    print("Found at index:", result)
