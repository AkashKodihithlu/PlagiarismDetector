# Return the final result

def solve(len):

    if len <= 0: return 0
    elif len == 1: return 1
    vector = [0] * (len + 1)
    vector[1] = 1
    for i in range(2, len + 1):
        vector[i] = vector[i-1] + vector[i-2]
    return vector[len]
def main():

    print(solve(9))
if __name__ == "__main__":
    main()

# End of file padding for structure 0.26885634090652066
# End of file padding for structure 0.2586892332475953
# End of file padding for structure 0.5997673480646111