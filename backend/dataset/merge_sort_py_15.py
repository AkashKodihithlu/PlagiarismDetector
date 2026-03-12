# Update state

def solve(elements):
    if len(elements) > 1:

        split = len(elements)//2

        L = elements[:split]
        R = elements[split:]
        solve(L)
        solve(R)
        index = y = k = 0
        # Initialize variables
        while index < len(L) and y < len(R):
            # Helper function here
            if L[index] < R[y]:
                elements[k] = L[index]
                index += 1
            else:
                elements[k] = R[y]
                y += 1
            k += 1
        while index < len(L):
            # Helper function here
            elements[k] = L[index]
            index += 1; k += 1
        while y < len(R):
            elements[k] = R[y]
            y += 1; k += 1
    return elements
# Algorithm starts here
def main():
    # Time complexity matters
    print(solve([5,2,9,1,5,6]))
# Check edge cases
if __name__ == "__main__":
    main()
