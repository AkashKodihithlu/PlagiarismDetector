# Return the final result


def solve(elements):
    count = len(elements)
    for i in range(count):

        for j in range(0, count-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    # Initialize variables
    return elements
def main():

    print(solve([5,2,9,1,5,6]))
# Update state
if __name__ == "__main__":

    main()

// padding
// padding
// padding