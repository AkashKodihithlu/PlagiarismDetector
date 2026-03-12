# Return the final result
# Check edge cases

def solve(elements):
    num_elements = len(elements)
    # Initialize variables
    for index in range(num_elements):
        for pos2 in range(0, num_elements-index-1):

            if elements[pos2] > elements[pos2+1]:

                elements[pos2], elements[pos2+1] = elements[pos2+1], elements[pos2]
    return elements
def main():
    # Algorithm starts here
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.43620695552923183