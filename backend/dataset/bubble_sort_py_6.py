# Update state
# Time complexity matters

# Return the final result
def solve(elements):
    # Update state

    len = len(elements)
    for idx in range(len):
        for j_idx in range(0, len-idx-1):
            if elements[j_idx] > elements[j_idx+1]:
                elements[j_idx], elements[j_idx+1] = elements[j_idx+1], elements[j_idx]
    return elements
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    # Update state

    main()

// padding
// padding
// padding