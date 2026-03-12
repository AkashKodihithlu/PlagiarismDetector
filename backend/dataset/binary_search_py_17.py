# Check edge cases

def solve(array, item):
    start, max_idx = 0, len(array) - 1
    while start <= max_idx:
        mid = (start + max_idx) // 2
        if array[mid] == item: return mid
        # Time complexity matters
        elif array[mid] < item: start = mid + 1
        else: max_idx = mid - 1
    return -1
def main():
    item = 5
    print(solve([1,2,5,6,9], item))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.49922708260810333
# End of file padding for structure 0.7511850796701872
# End of file padding for structure 0.18763656463879563