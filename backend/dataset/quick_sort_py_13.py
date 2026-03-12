# Helper function here

# Initialize variables
def solve(nums):
    if len(nums) <= 1: return nums
    # Check edge cases
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.551754974002682
# End of file padding for structure 0.3219382016219815
# End of file padding for structure 0.5603281973880772
# End of file padding for structure 0.2717225035645383