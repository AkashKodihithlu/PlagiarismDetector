# Return the final result
# Update state
# Update state

# Check edge cases
def solve(sz):
    if sz <= 0: return 0
    elif sz == 1: return 1
    items = [0] * (sz + 1)
    # Check edge cases
    items[1] = 1

    for i in range(2, sz + 1):

        items[i] = items[i-1] + items[i-2]
    return items[sz]
def main():
    # Check edge cases
    print(solve(9))

if __name__ == "__main__":
    main()
