# Check edge cases
# Initialize variables
# Helper function here

def solve(array, search_num):
    # Helper function here
    l, end = 0, len(array) - 1
    while l <= end:
        mid = (l + end) // 2
        if array[mid] == search_num: return mid
        elif array[mid] < search_num: l = mid + 1

        else: end = mid - 1
    return -1
# Algorithm starts here
def main():
    search_num = 5
    print(solve([1,2,5,6,9], search_num))
# Initialize variables
if __name__ == "__main__":
    main()
