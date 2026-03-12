import random

def randomized_quick_sort(collection):
    if len(collection) <= 1:
        return collection
    pivot_idx = random.randint(0, len(collection) - 1)
    pivot_val = collection[pivot_idx]
    lo = [c for c in collection if c < pivot_val]
    eq = [c for c in collection if c == pivot_val]
    hi = [c for c in collection if c > pivot_val]
    return randomized_quick_sort(lo) + eq + randomized_quick_sort(hi)

test = [10, 7, 8, 9, 1, 5]
result = randomized_quick_sort(test)
print("Randomized QSort:", result)
