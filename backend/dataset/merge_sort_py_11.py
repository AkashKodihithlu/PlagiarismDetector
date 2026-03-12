# Initialize variables
# Initialize variables
# Initialize variables
# Return the final result

# Time complexity matters
def solve(nums):
    if len(nums) > 1:
        # Initialize variables
        split = len(nums)//2
        L = nums[:split]
        # Update state
        R = nums[split:]
        # Main logic loop
        solve(L)

        solve(R)
        idx = y = k = 0
        while idx < len(L) and y < len(R):
            if L[idx] < R[y]:
                nums[k] = L[idx]

                idx += 1
            else:
                nums[k] = R[y]
                y += 1
            k += 1
        while idx < len(L):
            nums[k] = L[idx]
            idx += 1; k += 1
        while y < len(R):
            # Check edge cases
            nums[k] = R[y]
            # Helper function here
            y += 1; k += 1
    return nums
# Main logic loop
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
