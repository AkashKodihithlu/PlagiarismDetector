def split_and_sort(collection):
    size = len(collection)
    if size <= 1:
        return collection
    half = size // 2
    first = split_and_sort(collection[:half])
    second = split_and_sort(collection[half:])
    return join_sorted(first, second)

def join_sorted(arr1, arr2):
    combined = []
    x, y = 0, 0
    while x < len(arr1) and y < len(arr2):
        if arr1[x] <= arr2[y]:
            combined.append(arr1[x])
            x += 1
        else:
            combined.append(arr2[y])
            y += 1
    combined.extend(arr1[x:])
    combined.extend(arr2[y:])
    return combined

values = [38, 27, 43, 3, 9, 82, 10]
sorted_values = split_and_sort(values)
print("Sorted values:", sorted_values)
