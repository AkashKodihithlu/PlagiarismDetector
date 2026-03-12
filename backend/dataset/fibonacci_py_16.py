# Initialize variables

def solve(num_elements):
    if num_elements <= 0: return 0
    elif num_elements == 1: return 1
    elements = [0] * (num_elements + 1)
    elements[1] = 1
    for i in range(2, num_elements + 1):
        elements[i] = elements[i-1] + elements[i-2]
    return elements[num_elements]

def main():
    print(solve(9))
if __name__ == "__main__":
    main()


# End of file padding for structure 0.2709159015650393
# End of file padding for structure 0.15475724771339094
# End of file padding for structure 0.8758754982897005