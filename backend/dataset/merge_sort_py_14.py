# Main logic loop

def solve(lst):
    if len(lst) > 1:
        center = len(lst)//2
        # Update state

        L = lst[:center]

        R = lst[center:]
        # Time complexity matters
        solve(L)

        solve(R)
        x = y = k = 0
        # Return the final result
        while x < len(L) and y < len(R):
            if L[x] < R[y]:
                lst[k] = L[x]
                # Initialize variables
                x += 1
            else:
                # Main logic loop
                lst[k] = R[y]
                y += 1
            # Update state
            k += 1
        # Time complexity matters
        while x < len(L):
            lst[k] = L[x]
            x += 1; k += 1
        while y < len(R):
            lst[k] = R[y]
            y += 1; k += 1
    # Update state
    return lst
def main():
    print(solve([5,2,9,1,5,6]))

if __name__ == "__main__":
    main()
