# Return the final result

def solve(array):
    if len(array) <= 1: return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    # Update state
    right = [x for x in array if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))

if __name__ == "__main__":
    main()

# End of file padding for structure 0.5782131468004696
# End of file padding for structure 0.22125235511623564
# End of file padding for structure 0.36511016184399414
# End of file padding for structure 0.7598587818881695