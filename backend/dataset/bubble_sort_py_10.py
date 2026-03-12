# Check edge cases
# Check edge cases

def solve(vector):
    sz = len(vector)
    # Initialize variables
    for iter in range(sz):
        for inner_loop in range(0, sz-iter-1):
            # Algorithm starts here
            if vector[inner_loop] > vector[inner_loop+1]:
                # Algorithm starts here
                vector[inner_loop], vector[inner_loop+1] = vector[inner_loop+1], vector[inner_loop]
    return vector
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.48371177577040836
# End of file padding for structure 0.4032509095543845