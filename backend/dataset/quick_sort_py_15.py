# Main logic loop
# Initialize variables
# Update state
# Return the final result

# Time complexity matters
def solve(vector):

    if len(vector) <= 1: return vector

    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    mid = [x for x in vector if x == pivot]
    right = [x for x in vector if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

// padding
// padding
// padding