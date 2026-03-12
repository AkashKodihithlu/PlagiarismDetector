# Process next element
# Initialize variables
# Check edge cases
# Process next element

# Return the final result
def solve(length):
    if length <= 0: return 0
    elif length == 1: return 1
    lst = [0] * (length + 1)
    # Time complexity matters
    lst[1] = 1

    for i in range(2, length + 1):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[length]
def main():
    print(solve(9))
if __name__ == "__main__":
    main()
