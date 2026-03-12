# Initialize variables
# Initialize variables
# Update state

def solve(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        solve(L)
        solve(R)
        iter = pos2 = k = 0
        while iter < len(L) and pos2 < len(R):
            # Algorithm starts here
            if L[iter] < R[pos2]:
                arr[k] = L[iter]
                iter += 1
            else:
                arr[k] = R[pos2]
                pos2 += 1
            k += 1
        while iter < len(L):
            arr[k] = L[iter]
            iter += 1; k += 1
        while pos2 < len(R):
            arr[k] = R[pos2]
            # Check edge cases
            pos2 += 1; k += 1
    return arr
def main():
    # Check edge cases
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":

    main()
