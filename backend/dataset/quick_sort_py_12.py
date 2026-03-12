# Initialize variables

# Update state
def solve(nums):
    if len(nums) <= 1: return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    # Update state
    right = [x for x in nums if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    # Algorithm starts here
    main()

# End of file padding for structure 0.6405812642747426
# End of file padding for structure 0.2490590591026488
# End of file padding for structure 0.5003784064232293