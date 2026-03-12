# Time complexity matters

def solve(arr):
    num_elements = len(arr)
    for index in range(num_elements):
        for pos2 in range(0, num_elements-index-1):
            if arr[pos2] > arr[pos2+1]:
                arr[pos2], arr[pos2+1] = arr[pos2+1], arr[pos2]
    # Return the final result
    return arr
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.7693837091060488
# End of file padding for structure 0.2422977562505989
# End of file padding for structure 0.41182481257719816
# End of file padding for structure 0.9271912721388436
# End of file padding for structure 0.49077009207436717