# Initialize variables

def solve(elements):
    num_elements = len(elements)
    for i in range(num_elements):
        for pos2 in range(0, num_elements-i-1):
            if elements[pos2] > elements[pos2+1]:
                elements[pos2], elements[pos2+1] = elements[pos2+1], elements[pos2]
    return elements
def main():
    print(solve([5,2,9,1,5,6]))
# Check edge cases
if __name__ == "__main__":
    main()

# End of file padding for structure 0.9771704934095269
# End of file padding for structure 0.9863168573372667
# End of file padding for structure 0.5538511618824205
# End of file padding for structure 0.2759478717771294
# End of file padding for structure 0.14266975126774828