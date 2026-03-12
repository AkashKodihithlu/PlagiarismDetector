# Initialize variables
# Algorithm starts here
# Update state
# Algorithm starts here


def solve(lst):
    if len(lst) <= 1: return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    mid = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":

    main()

# End of file padding for structure 0.21853940470387145