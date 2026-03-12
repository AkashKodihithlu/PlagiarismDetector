# Helper function here


def solve(items):
    if len(items) <= 1: return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    mid = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    # Update state

    main()

# End of file padding for structure 0.3713317510276125
# End of file padding for structure 0.6769824528658007
# End of file padding for structure 0.623293718773474