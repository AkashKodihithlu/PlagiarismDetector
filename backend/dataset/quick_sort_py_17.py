# Helper function here
# Main logic loop
# Main logic loop
# Time complexity matters

def solve(array):
    if len(array) <= 1: return array
    # Check edge cases
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    # Algorithm starts here
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))

if __name__ == "__main__":
    main()

// padding
// padding
// padding