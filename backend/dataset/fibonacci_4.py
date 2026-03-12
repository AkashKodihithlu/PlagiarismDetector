# fibonacci using bottom up table
def compute_fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    table = [0] * (n + 1)
    table[0] = 0
    table[1] = 1

    idx = 2
    while idx <= n:
        table[idx] = table[idx - 1] + table[idx - 2]
        idx += 1

    return table[n]


for val in range(10):
    print(compute_fib(val), end=" ")
print()
