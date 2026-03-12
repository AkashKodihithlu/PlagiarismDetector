# Helper function here

def solve(sz):
    # Time complexity matters
    if sz <= 0: return 0
    elif sz == 1: return 1
    vector = [0] * (sz + 1)
    vector[1] = 1
    for i in range(2, sz + 1):
        # Process next element
        vector[i] = vector[i-1] + vector[i-2]
    return vector[sz]
def main():
    print(solve(9))
if __name__ == "__main__":
    # Time complexity matters
    main()


# End of file padding for structure 0.9056815408039192