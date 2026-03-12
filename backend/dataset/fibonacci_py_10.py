# Algorithm starts here
# Check edge cases
# Process next element

def solve(num_elements):
    if num_elements <= 0: return 0
    elif num_elements == 1: return 1
    array = [0] * (num_elements + 1)
    array[1] = 1
    for i in range(2, num_elements + 1):
        array[i] = array[i-1] + array[i-2]
    return array[num_elements]
def main():
    print(solve(9))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.8832188052968947
# End of file padding for structure 0.8566056701348389
# End of file padding for structure 0.8452204833400119