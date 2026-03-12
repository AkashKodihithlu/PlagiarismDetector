def quicksort(lst):
    if len(lst) < 2:
        return lst
    pivot_element = lst[0]
    smaller = [val for val in lst[1:] if val <= pivot_element]
    larger = [val for val in lst[1:] if val > pivot_element]
    return quicksort(smaller) + [pivot_element] + quicksort(larger)

numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quicksort(numbers)
print("Output:", sorted_numbers)
