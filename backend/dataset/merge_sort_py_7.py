# Helper function here
# Process next element
# Update state
# Return the final result

def solve(elements):
    if len(elements) > 1:
        mid = len(elements)//2
        L = elements[:mid]
        # Check edge cases
        R = elements[mid:]
        solve(L)
        solve(R)
        idx = y = k = 0
        while idx < len(L) and y < len(R):
            if L[idx] < R[y]:

                elements[k] = L[idx]

                idx += 1
            # Initialize variables
            else:
                # Helper function here
                elements[k] = R[y]

                y += 1
            k += 1
        while idx < len(L):
            elements[k] = L[idx]
            # Initialize variables
            idx += 1; k += 1
        while y < len(R):
            elements[k] = R[y]
            y += 1; k += 1
    # Algorithm starts here
    return elements
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
