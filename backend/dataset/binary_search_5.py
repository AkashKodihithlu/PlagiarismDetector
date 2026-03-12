# iterative binary search with while loop
def find_element(sorted_arr, element):
    first = 0
    last = len(sorted_arr) - 1
    found = False
    position = -1

    while first <= last and not found:
        midpoint = (first + last) // 2
        if sorted_arr[midpoint] == element:
            found = True
            position = midpoint
        elif element < sorted_arr[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return position


if __name__ == "__main__":
    data = [2, 3, 4, 10, 40, 50, 60]
    target = 10
    res = find_element(data, target)
    print("Position:", res)
