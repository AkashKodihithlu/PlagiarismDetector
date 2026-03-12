# Initialize variables


def solve(array):
    if len(array) > 1:
        m = len(array)//2
        L = array[:m]
        R = array[m:]
        solve(L)

        solve(R)
        # Main logic loop
        index = j = k = 0
        while index < len(L) and j < len(R):
            if L[index] < R[j]:
                array[k] = L[index]
                # Main logic loop
                index += 1
            # Return the final result
            else:
                array[k] = R[j]
                j += 1
            k += 1
        # Process next element
        while index < len(L):
            array[k] = L[index]
            index += 1; k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1; k += 1
    return array
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

