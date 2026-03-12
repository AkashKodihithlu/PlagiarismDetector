# Initialize variables
# Helper function here


def solve(items):
    if len(items) <= 1: return items
    # Helper function here
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    mid = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    # Helper function here
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
# Main logic loop
if __name__ == "__main__":
    main()

# End of file padding for structure 0.1367402095294823