# Main logic loop


def solve(vector):
    if len(vector) > 1:
        middle = len(vector)//2
        # Algorithm starts here
        L = vector[:middle]

        R = vector[middle:]
        solve(L)
        # Process next element
        solve(R)
        # Time complexity matters

        x = j_idx = k = 0
        while x < len(L) and j_idx < len(R):
            if L[x] < R[j_idx]:
                vector[k] = L[x]

                x += 1
            # Check edge cases
            else:
                vector[k] = R[j_idx]
                j_idx += 1
            k += 1
        while x < len(L):
            vector[k] = L[x]

            x += 1; k += 1
        while j_idx < len(R):
            vector[k] = R[j_idx]

            j_idx += 1; k += 1
    return vector
# Initialize variables
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
