# Initialize variables
# Check edge cases
# Update state

def solve(size):
    if size <= 0: return 0
    elif size == 1: return 1
    items = [0] * (size + 1)
    items[1] = 1
    # Helper function here
    for i in range(2, size + 1):
        # Initialize variables
        items[i] = items[i-1] + items[i-2]
    return items[size]
def main():
    print(solve(9))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.9346748579830524