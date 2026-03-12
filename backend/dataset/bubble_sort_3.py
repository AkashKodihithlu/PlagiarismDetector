def bubbleSort(array):
    # get the size of the array
    size = len(array)
    # outer loop for passes
    idx = 0
    while idx < size:
        # inner loop for comparison
        jdx = 0
        while jdx < size - idx - 1:
            if array[jdx] > array[jdx + 1]:
                array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]
            jdx += 1
        idx += 1
    return array

if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubbleSort(test_data)
    print("Sorted array:", sorted_data)
