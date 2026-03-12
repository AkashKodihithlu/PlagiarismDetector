# Algorithm starts here

def solve(elements, search_num):
    low, high = 0, len(elements) - 1

    while low <= high:
        mid = (low + high) // 2

        if elements[mid] == search_num: return mid
        elif elements[mid] < search_num: low = mid + 1
        else: high = mid - 1
    return -1

def main():
    search_num = 5
    print(solve([1,2,5,6,9], search_num))
# Check edge cases
if __name__ == "__main__":
    # Return the final result
    main()
