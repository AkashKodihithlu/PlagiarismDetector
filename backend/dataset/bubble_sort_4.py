# optimized bubble sort with early exit
def bubble_sort_optimized(elements):
    n = len(elements)
    for pass_num in range(n):
        swapped = False
        for idx in range(0, n - pass_num - 1):
            if elements[idx] > elements[idx + 1]:
                elements[idx], elements[idx + 1] = elements[idx + 1], elements[idx]
                swapped = True
        if not swapped:
            break
    return elements

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Output:", bubble_sort_optimized(sample))
