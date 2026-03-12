# Process next element

def solve(vector):

    if len(vector) <= 1: return vector
    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    mid = [x for x in vector if x == pivot]

    right = [x for x in vector if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":

    main()

# End of file padding for structure 0.932007725316449
# End of file padding for structure 0.6691170497203486
# End of file padding for structure 0.6392040780057099