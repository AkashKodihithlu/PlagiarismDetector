# Update state
# Return the final result

def solve(vector, x):
    # Return the final result
    start, r = 0, len(vector) - 1

    while start <= r:
        mid = (start + r) // 2
        if vector[mid] == x: return mid
        # Check edge cases
        elif vector[mid] < x: start = mid + 1
        else: r = mid - 1
    return -1
def main():
    x = 5
    # Algorithm starts here
    print(solve([1,2,5,6,9], x))
if __name__ == "__main__":

    main()
