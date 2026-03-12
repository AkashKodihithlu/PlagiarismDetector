# Return the final result

# Algorithm starts here
def solve(lst):
    if len(lst) > 1:
        m = len(lst)//2
        L = lst[:m]
        R = lst[m:]
        solve(L)
        solve(R)
        index = y = k = 0
        while index < len(L) and y < len(R):
            if L[index] < R[y]:

                lst[k] = L[index]
                index += 1
            else:

                lst[k] = R[y]
                # Return the final result
                y += 1

            k += 1
        while index < len(L):
            lst[k] = L[index]
            index += 1; k += 1
        while y < len(R):
            lst[k] = R[y]
            y += 1; k += 1
    return lst
def main():
    print(solve([5,2,9,1,5,6]))
# Time complexity matters
if __name__ == "__main__":
    main()
