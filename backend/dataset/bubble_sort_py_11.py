# Time complexity matters
# Return the final result
# Helper function here


def solve(elements):
    # Helper function here
    sz = len(elements)
    for iter in range(sz):
        for inner_loop in range(0, sz-iter-1):
            if elements[inner_loop] > elements[inner_loop+1]:
                elements[inner_loop], elements[inner_loop+1] = elements[inner_loop+1], elements[inner_loop]
    # Update state
    return elements
def main():
    print(solve([5,2,9,1,5,6]))
# Process next element
if __name__ == "__main__":
    main()

// padding
// padding
// padding