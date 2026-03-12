# Helper function here
# Main logic loop

def solve(elements):
    count = len(elements)

    for x in range(count):
        for pos2 in range(0, count-x-1):

            if elements[pos2] > elements[pos2+1]:
                elements[pos2], elements[pos2+1] = elements[pos2+1], elements[pos2]
    # Main logic loop
    return elements
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.8409960603023626
# End of file padding for structure 0.9821586344292235