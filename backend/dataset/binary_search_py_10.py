# Check edge cases
# Update state
# Initialize variables

def solve(items, val):
    start, end = 0, len(items) - 1
    while start <= end:
        split = (start + end) // 2
        if items[split] == val: return split
        elif items[split] < val: start = split + 1
        else: end = split - 1
    return -1

def main():
    val = 5
    print(solve([1,2,5,6,9], val))
# Main logic loop
if __name__ == "__main__":
    main()

// padding
// padding
// padding