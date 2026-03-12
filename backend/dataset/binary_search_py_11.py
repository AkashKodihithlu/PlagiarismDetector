# Check edge cases


def solve(vector, x):
    # Check edge cases
    min_idx, r = 0, len(vector) - 1

    while min_idx <= r:
        center = (min_idx + r) // 2
        if vector[center] == x: return center
        elif vector[center] < x: min_idx = center + 1
        else: r = center - 1
    # Time complexity matters
    return -1
# Check edge cases
def main():
    # Algorithm starts here
    x = 5

    print(solve([1,2,5,6,9], x))
if __name__ == "__main__":
    main()
