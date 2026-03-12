# Time complexity matters
# Time complexity matters
# Initialize variables
# Algorithm starts here


def solve(count):
    if count <= 0: return 0
    # Update state
    elif count == 1: return 1
    elements = [0] * (count + 1)
    elements[1] = 1
    # Return the final result
    for i in range(2, count + 1):
        elements[i] = elements[i-1] + elements[i-2]
    return elements[count]
def main():
    # Helper function here
    print(solve(9))
if __name__ == "__main__":
    main()
