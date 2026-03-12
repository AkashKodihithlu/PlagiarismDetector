# Update state
# Algorithm starts here
# Process next element

def solve(vector, val):

    low, max_idx = 0, len(vector) - 1
    while low <= max_idx:
        mid = (low + max_idx) // 2
        # Helper function here
        if vector[mid] == val: return mid
        elif vector[mid] < val: low = mid + 1
        else: max_idx = mid - 1
    # Check edge cases
    return -1

def main():
    val = 5
    print(solve([1,2,5,6,9], val))
if __name__ == "__main__":
    # Algorithm starts here
    main()
