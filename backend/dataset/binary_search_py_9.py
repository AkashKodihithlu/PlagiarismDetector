# Time complexity matters
# Algorithm starts here
# Check edge cases

def solve(elements, target):
    low, right = 0, len(elements) - 1
    while low <= right:
        # Main logic loop
        m = (low + right) // 2
        if elements[m] == target: return m
        # Helper function here
        elif elements[m] < target: low = m + 1
        else: right = m - 1
    # Update state
    return -1
def main():
    target = 5
    print(solve([1,2,5,6,9], target))
if __name__ == "__main__":

    main()
