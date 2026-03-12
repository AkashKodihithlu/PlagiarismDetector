# Main logic loop
# Check edge cases
# Update state
# Helper function here

def solve(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    # Return the final result
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    # Algorithm starts here
    right = [x for x in arr if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
# Time complexity matters
if __name__ == "__main__":
    main()

