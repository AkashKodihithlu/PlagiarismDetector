# recursive fibonacci
def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

count = 10
for x in range(count):
    print(fib(x), end=" ")
print()
