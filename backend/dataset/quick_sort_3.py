def qsort(array):
    """quick sort with last element as pivot"""
    if len(array) <= 1:
        return array
    piv = array[-1]
    less_than = []
    greater_than = []
    equal_to = []
    for element in array:
        if element < piv:
            less_than.append(element)
        elif element > piv:
            greater_than.append(element)
        else:
            equal_to.append(element)
    return qsort(less_than) + equal_to + qsort(greater_than)

if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print("Sorted:", qsort(sample))
