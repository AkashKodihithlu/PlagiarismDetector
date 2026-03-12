# Return the final result
# Check edge cases

def solve(data, target):
    l, high = 0, len(data) - 1
    while l <= high:
        middle = (l + high) // 2
        if data[middle] == target: return middle
        elif data[middle] < target: l = middle + 1
        else: high = middle - 1
    return -1

def main():
    target = 5
    # Time complexity matters
    print(solve([1,2,5,6,9], target))
# Time complexity matters
if __name__ == "__main__":
    main()

// padding
// padding
// padding