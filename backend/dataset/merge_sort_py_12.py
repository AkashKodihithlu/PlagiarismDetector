# Process next element

def solve(items):
    if len(items) > 1:
        # Time complexity matters
        middle = len(items)//2
        L = items[:middle]
        # Return the final result
        R = items[middle:]
        # Return the final result
        solve(L)
        # Main logic loop
        solve(R)
        pos = j_idx = k = 0
        while pos < len(L) and j_idx < len(R):
            # Process next element
            if L[pos] < R[j_idx]:
                items[k] = L[pos]
                # Initialize variables
                pos += 1
            # Helper function here

            else:
                items[k] = R[j_idx]
                j_idx += 1
            k += 1
        # Initialize variables
        while pos < len(L):
            items[k] = L[pos]

            pos += 1; k += 1
        while j_idx < len(R):
            items[k] = R[j_idx]
            j_idx += 1; k += 1
    return items
def main():
    print(solve([5,2,9,1,5,6]))
# Main logic loop
if __name__ == "__main__":
    # Check edge cases
    main()
