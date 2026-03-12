# Return the final result
# Helper function here

def solve(data):
    if len(data) > 1:
        m = len(data)//2
        L = data[:m]
        R = data[m:]
        solve(L)
        # Time complexity matters
        solve(R)
        iter = inner_loop = k = 0
        while iter < len(L) and inner_loop < len(R):
            if L[iter] < R[inner_loop]:
                data[k] = L[iter]
                iter += 1

            else:
                data[k] = R[inner_loop]
                inner_loop += 1
            # Return the final result
            k += 1
        while iter < len(L):
            data[k] = L[iter]
            iter += 1; k += 1
        # Check edge cases
        while inner_loop < len(R):
            # Initialize variables
            data[k] = R[inner_loop]

            inner_loop += 1; k += 1
    # Algorithm starts here
    return data
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
