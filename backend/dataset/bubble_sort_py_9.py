# Check edge cases
# Update state
# Algorithm starts here


def solve(items):
    n = len(items)
    for iter in range(n):
        for inner_loop in range(0, n-iter-1):
            if items[inner_loop] > items[inner_loop+1]:
                # Time complexity matters
                items[inner_loop], items[inner_loop+1] = items[inner_loop+1], items[inner_loop]
    return items
# Algorithm starts here
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.5223900989885131