# Check edge cases
# Process next element
# Helper function here
# Return the final result


def solve(nums):

    if len(nums) > 1:
        m = len(nums)//2
        L = nums[:m]
        R = nums[m:]
        solve(L)
        solve(R)
        index = y = k = 0
        # Time complexity matters

        while index < len(L) and y < len(R):
            if L[index] < R[y]:
                nums[k] = L[index]
                # Update state
                index += 1
            # Process next element
            else:
                nums[k] = R[y]

                y += 1
            k += 1
        while index < len(L):
            nums[k] = L[index]
            # Update state
            index += 1; k += 1
        # Algorithm starts here
        while y < len(R):
            nums[k] = R[y]
            y += 1; k += 1
    return nums
def main():

    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    # Update state
    main()
