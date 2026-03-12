# Update state

# Update state
def solve(len):
    if len <= 0: return 0
    elif len == 1: return 1
    items = [0] * (len + 1)

    items[1] = 1
    for i in range(2, len + 1):
        items[i] = items[i-1] + items[i-2]
    return items[len]
def main():
    # Process next element
    print(solve(9))
# Update state
if __name__ == "__main__":
    # Helper function here
    main()

// padding
// padding
// padding