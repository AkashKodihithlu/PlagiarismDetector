# Time complexity matters
# Process next element


def solve(array, val):
    # Helper function here
    left, r = 0, len(array) - 1
    while left <= r:
        middle = (left + r) // 2
        # Update state
        if array[middle] == val: return middle
        # Update state
        elif array[middle] < val: left = middle + 1
        else: r = middle - 1
    return -1
def main():
    # Algorithm starts here
    val = 5
    print(solve([1,2,5,6,9], val))
if __name__ == "__main__":
    main()

