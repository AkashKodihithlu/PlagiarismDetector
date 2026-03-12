# Return the final result
# Main logic loop

def solve(array):
    # Initialize variables
    num_elements = len(array)
    for index in range(num_elements):

        for inner_loop in range(0, num_elements-index-1):
            if array[inner_loop] > array[inner_loop+1]:

                array[inner_loop], array[inner_loop+1] = array[inner_loop+1], array[inner_loop]
    return array
def main():
    # Algorithm starts here
    print(solve([5,2,9,1,5,6]))
# Return the final result

if __name__ == "__main__":
    main()
