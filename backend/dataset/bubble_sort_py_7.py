# Update state

# Process next element
def solve(data):
    # Return the final result
    size = len(data)
    for idx in range(size):
        for y in range(0, size-idx-1):
            if data[y] > data[y+1]:
                data[y], data[y+1] = data[y+1], data[y]

    return data
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.3117119770645166
# End of file padding for structure 0.3129954059537108
# End of file padding for structure 0.1612055851083718