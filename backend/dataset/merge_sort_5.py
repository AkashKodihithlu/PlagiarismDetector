# in-place style merge sort
def m_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l_half = arr[:m]
        r_half = arr[m:]

        m_sort(l_half)
        m_sort(r_half)

        i = j = k = 0
        while i < len(l_half) and j < len(r_half):
            if l_half[i] < r_half[j]:
                arr[k] = l_half[i]
                i += 1
            else:
                arr[k] = r_half[j]
                j += 1
            k += 1

        while i < len(l_half):
            arr[k] = l_half[i]
            i += 1
            k += 1

        while j < len(r_half):
            arr[k] = r_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    m_sort(data)
    print("Sorted:", data)
