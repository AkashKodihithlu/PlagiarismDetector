# merge sort algorithm
def mergesort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst) // 2
    left_half = mergesort(lst[:middle])
    right_half = mergesort(lst[middle:])
    return combine(left_half, right_half)

def combine(a, b):
    merged = []
    idx_a = 0
    idx_b = 0
    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            merged.append(a[idx_a])
            idx_a += 1
        else:
            merged.append(b[idx_b])
            idx_b += 1
    while idx_a < len(a):
        merged.append(a[idx_a])
        idx_a += 1
    while idx_b < len(b):
        merged.append(b[idx_b])
        idx_b += 1
    return merged

nums = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(nums))
