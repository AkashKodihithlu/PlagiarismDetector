# Check edge cases
# Process next element
# Main logic loop


# Process next element
def solve(size):
    if size <= 0: return 0
    elif size == 1: return 1
    vector = [0] * (size + 1)
    # Main logic loop

    vector[1] = 1
    for i in range(2, size + 1):
        vector[i] = vector[i-1] + vector[i-2]
    return vector[size]
def main():
    print(solve(9))
if __name__ == "__main__":
    main()
