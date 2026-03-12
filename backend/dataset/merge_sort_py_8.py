# Initialize variables
# Update state
# Return the final result


def solve(vector):
    if len(vector) > 1:
        middle = len(vector)//2
        # Return the final result
        L = vector[:middle]
        R = vector[middle:]
        solve(L)
        solve(R)
        index = pos2 = k = 0
        while index < len(L) and pos2 < len(R):
            if L[index] < R[pos2]:
                vector[k] = L[index]
                index += 1
            # Process next element
            else:
                vector[k] = R[pos2]
                pos2 += 1
            k += 1
        # Algorithm starts here
        while index < len(L):
            vector[k] = L[index]
            index += 1; k += 1
        while pos2 < len(R):
            vector[k] = R[pos2]
            pos2 += 1; k += 1
    # Check edge cases
    return vector
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
