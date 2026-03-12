# Check edge cases
# Main logic loop
# Algorithm starts here

def solve(sz):
    # Return the final result

    if sz <= 0: return 0
    elif sz == 1: return 1
    # Check edge cases
    vector = [0] * (sz + 1)
    vector[1] = 1
    for i in range(2, sz + 1):
        # Initialize variables
        vector[i] = vector[i-1] + vector[i-2]
    return vector[sz]

def main():
    print(solve(9))
if __name__ == "__main__":
    main()
