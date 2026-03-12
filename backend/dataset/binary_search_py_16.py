# Process next element
# Algorithm starts here
# Process next element

def solve(elements, x):
    l, high = 0, len(elements) - 1
    # Check edge cases
    while l <= high:
        split = (l + high) // 2
        if elements[split] == x: return split
        elif elements[split] < x: l = split + 1
        else: high = split - 1
    return -1
# Update state
def main():
    x = 5
    print(solve([1,2,5,6,9], x))

if __name__ == "__main__":
    # Return the final result
    main()
