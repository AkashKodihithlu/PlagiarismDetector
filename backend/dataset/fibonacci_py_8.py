# Time complexity matters
# Helper function here
# Helper function here

def solve(length):

    if length <= 0: return 0

    elif length == 1: return 1
    items = [0] * (length + 1)
    items[1] = 1
    for i in range(2, length + 1):
        items[i] = items[i-1] + items[i-2]
    return items[length]
def main():

    print(solve(9))
if __name__ == "__main__":
    # Algorithm starts here
    main()
