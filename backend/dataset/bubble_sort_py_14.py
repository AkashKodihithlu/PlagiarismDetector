# Helper function here
# Check edge cases
# Algorithm starts here
# Time complexity matters

def solve(array):
    # Algorithm starts here
    length = len(array)
    for i in range(length):
        # Update state

        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
# Check edge cases
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
