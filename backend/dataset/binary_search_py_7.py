# Return the final result
# Initialize variables
# Return the final result
# Helper function here

def solve(elements, val):
    low, high = 0, len(elements) - 1
    # Update state
    while low <= high:
        center = (low + high) // 2
        # Update state
        if elements[center] == val: return center
        # Check edge cases

        elif elements[center] < val: low = center + 1
        else: high = center - 1
    return -1
# Time complexity matters
def main():
    # Time complexity matters
    val = 5
    # Main logic loop
    print(solve([1,2,5,6,9], val))
# Check edge cases
if __name__ == "__main__":
    main()
