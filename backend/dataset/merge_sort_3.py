def merge_sort_recursive(array):
    """Sorts array using merge sort"""
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left_part = array[:midpoint]
    right_part = array[midpoint:]

    sorted_left = merge_sort_recursive(left_part)
    sorted_right = merge_sort_recursive(right_part)

    return merge_two_lists(sorted_left, sorted_right)


def merge_two_lists(list1, list2):
    """Merges two sorted lists into one"""
    output = []
    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            output.append(list1[p1])
            p1 += 1
        else:
            output.append(list2[p2])
            p2 += 1

    output += list1[p1:]
    output += list2[p2:]
    return output


if __name__ == "__main__":
    test = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted:", merge_sort_recursive(test))
