def bsearch(lst, item):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if lst[m] == item:
            return m
        if lst[m] > item:
            hi = m - 1
        else:
            lo = m + 1
    return -1

arr = [2, 3, 4, 10, 40, 50, 60]
print("Index:", bsearch(arr, 10))
print("Index:", bsearch(arr, 99))
