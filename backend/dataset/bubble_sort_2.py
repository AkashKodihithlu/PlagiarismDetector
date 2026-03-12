# Sorting using bubble technique
def sort_bubble(lst):
    length = len(lst)
    for outer in range(length):
        for inner in range(0, length - outer - 1):
            if lst[inner] > lst[inner + 1]:
                temp = lst[inner]
                lst[inner] = lst[inner + 1]
                lst[inner + 1] = temp
    return lst

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    result = sort_bubble(numbers)
    print("Result:", result)
