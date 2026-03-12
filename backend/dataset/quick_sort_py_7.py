# Return the final result

def solve(nums):

    if len(nums) <= 1: return nums
    # Return the final result
    pivot = nums[len(nums) // 2]
    # Initialize variables
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    # Algorithm starts here
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    # Initialize variables
    main()


// padding
// padding
// padding